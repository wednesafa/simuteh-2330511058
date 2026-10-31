
import json
import os
import cv2
import numpy as np

PARAM_BAWAAN = {
    "lebar": 640,
    "gamma": 1.0,
    "clahe_clip": 2.0,
    "clahe_tile": 8,
    "penapis": "median",
    "kernel": 3,
    "sigma": 1.0,
    "tajam_k": 0.0,
}

def praproses(img_bgr, p=None):
    p = {**PARAM_BAWAAN, **(p or {})}

    # TODO 1: Ubah ukuran
    tinggi, lebar = img_bgr.shape[:2]
    tinggi_baru = int(tinggi * p["lebar"] / lebar)

    img = cv2.resize(
        img_bgr,
        (p["lebar"], tinggi_baru),
        interpolation=cv2.INTER_AREA
    )

    # TODO 2: Koreksi gamma
    if p["gamma"] != 1:
        tabel = np.array([
            ((i / 255.0) ** (1.0 / p["gamma"])) * 255
            for i in range(256)
        ]).clip(0, 255).astype("uint8")

        img = cv2.LUT(img, tabel)

    # TODO 3: CLAHE kanal V
    if p["clahe_clip"] > 0:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        clahe = cv2.createCLAHE(
            clipLimit=p["clahe_clip"],
            tileGridSize=(p["clahe_tile"], p["clahe_tile"])
        )

        hsv[:, :, 2] = clahe.apply(hsv[:, :, 2])
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # TODO 4: Redam derau
    kernel = p["kernel"]

    if p["penapis"] == "rerata":
        img = cv2.blur(img, (kernel, kernel))

    elif p["penapis"] == "gaussian":
        img = cv2.GaussianBlur(
            img, (kernel, kernel), p["sigma"]
        )

    elif p["penapis"] == "median":
        img = cv2.medianBlur(img, kernel)

    elif p["penapis"] == "none":
        pass

    else:
        raise ValueError("Jenis penapis tidak dikenal")

    # TODO 5: Tajamkan
    if p["tajam_k"] > 0:
        blur = cv2.GaussianBlur(img, (0, 0), 3)

        img = cv2.addWeighted(
            img, 1 + p["tajam_k"],
            blur, -p["tajam_k"],
            0
        )

    return img


def simpan_param(p, path="hasil/param_praproses.json"):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    with open(path, "w") as f:
        json.dump({**PARAM_BAWAAN, **p}, f, indent=2)
