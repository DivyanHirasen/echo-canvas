import requests
import os
import random
from urllib.parse import quote

def generate_pollinations_unified(
    prompt: str,
    api_key: str,                  # ← Your key from enter.pollinations.ai (sk_... or pk_...)
    width: int = 768,
    height: int = 1024,
    model: str = "flux",           # flux, flux-turbo, dirtberry-pro, etc.
    seed: int = None,
    save_path: str = "generated_image.jpg",
    enhance: bool = False,         # optional
    nologo: bool = True            # optional (many still support it)
):
    base_url = "https://gen.pollinations.ai/image/"
    
    # URL-encode the prompt
    encoded_prompt = quote(prompt)
    
    # Build query parameters
    params = {
        "model": model,
        "width": str(width),
        "height": str(height),
        "nologo": "true" if nologo else "false",
    }
    
    if seed is not None:
        params["seed"] = str(seed)
    if enhance:
        params["enhance"] = "true"
    
    # You can add more like negative_prompt=... if the model supports it
    
    full_url = base_url + encoded_prompt
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    
    try:
        response = requests.get(full_url, params=params, headers=headers, timeout=120)
        response.raise_for_status()
        
        content_type = response.headers.get("content-type", "")
        
        if "image/" not in content_type:
            print("Unexpected content-type:", content_type)
            print("Response:", response.text[:500])
            return None
        
        with open(save_path, "wb") as f:
            f.write(response.content)
        
        print(f"Image saved to: {os.path.abspath(save_path)}")
        print(f"Used URL: {response.url}")  # for debugging
        return save_path
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        if 'response' in locals():
            print("Status code:", response.status_code)
            print("Response details:", response.text)
        return None


# ─── Usage example ────────────────────────────────────────


prompt = "A haunting archaic watercolor painting of a lone figure on a misty cliff reaching toward distant golden light, dark moody atmosphere, heavy shadows, muted earthy tones with crimson and indigo accents, gothic romanticism style"

generate_pollinations_unified(
    prompt,
    YOUR_API_KEY,
    model="flux",
    width=896,          # flux often likes multiples of 64/128
    height=1152,
    seed=random.randint(0, 2147483647),
    nologo=True
)