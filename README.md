# Image-to-Normal-Map
**Create normal maps from images (using AI)**

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/estimating-and-exploiting-the-aleatoric/surface-normals-estimation-on-nyu-depth-v2-1)](https://paperswithcode.com/sota/surface-normals-estimation-on-nyu-depth-v2-1?p=estimating-and-exploiting-the-aleatoric)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/estimating-and-exploiting-the-aleatoric/surface-normals-estimation-on-scannetv2)](https://paperswithcode.com/sota/surface-normals-estimation-on-scannetv2?p=estimating-and-exploiting-the-aleatoric)

<img width=45% src="tests/oval-office-large.jpg"><img width=45% src="tests/oval-office-large-normal.jpg">

**Quick Start**
```bash
pip install imaginairy-normal-map
```

```python
from PIL import Image
from imaginairy_normal_map.model import create_normal_map_pil_img

img = Image.open("oval-office-large.jpg")
normal_img = create_normal_map_pil_img(img)
normal_img.save("oval-office-large-normal.jpg")
```


**This project was made to support the AI image generation project, [imaginAIry](https://github.com/brycedrennan/imaginAIry).**




**Credit to Gwangbin Bae, Ignas Budvytis, and Roberto Cipolla for creation of 
the [original algorithm and code](https://github.com/baegwangbin/surface_normal_uncertainty).**




<img width=70% src="https://github.com/baegwangbin/surface_normal_uncertainty/blob/main/figs/readme_scannet.png?raw=true">
<img width=100% src="https://github.com/baegwangbin/surface_normal_uncertainty/blob/main/figs/readme_generalize.png?raw=true">


