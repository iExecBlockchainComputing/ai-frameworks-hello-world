# 🧠 AI Frameworks Hello World

This repository provides minimal **"Hello, World!"** examples for several popular AI and numerical computing frameworks, each isolated in its own folder with a `Dockerfile` and `app.py`.

These examples are designed to:

- Quickly test basic functionality of each framework
- Run inside containerized environments
- **Work with Intel® TDX (Trust Domain Extensions)** out of the box

> ⚠️ While some frameworks include a `sconify.sh` script for SGX compatibility, **execution support is currently verified only for TDX**. See notes below.

---

## 📁 Repository Structure

```
ai-frameworks-hello-world/
├── tensorflow/
│   ├── app.py
│   └── Dockerfile
├── pytorch/
│   ├── app.py
│   └── Dockerfile
├── scikit/
│   ├── app.py
│   ├── Dockerfile
│   └── sconify.sh (not working on SGX)
├── openvino/
│   ├── app.py
│   ├── Dockerfile
│   └── sconify.sh (not working on SGX)
├── numpy/
│   ├── app.py
│   ├── Dockerfile
│   └── sconify.sh (not working on SGX)
```

Each `app.py` file contains a minimal script that initializes and runs a simple function with the corresponding framework (e.g., tensor addition, model inference, classification, etc.).

---

## ✅ Tested Frameworks

| Framework  | Version Range | Status on TDX | Notes on SGX          |
|------------|----------------|---------------|------------------------|
| TensorFlow | 2.19.0         | ✅ Supported   | –                      |
| PyTorch    | 2.7.0+cu126    | ✅ Supported   | –                      |
| Scikit-Learn | 1.6.1        | ✅ Supported   | ✅ Supported `sconify.sh` included |
| OpenVINO   | 2024.6.0       | ✅ Supported   | `sconify.sh` included, but execution issues on SGX |
| NumPy      | 2.0.2          | ✅ Supported   | ✅ Supported `sconify.sh` included |

---

## 🛡️ TDX Deployment

All examples are compatible and tested with [Intel® TDX](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-trust-domain-extensions.html).

📖 To learn how to build and run these containers inside a TDX guest environment, follow this guide:  
👉 **[Deploying Confidential iApp with TDX]([https://github.com/konveyor/tdx-tools/blob/main/docs/tdx-quickstart.md](https://protocol.docs.iex.ec/for-developers/confidential-computing/create-your-first-tdx-app))**

---

## 🔧 Usage

To build and run a specific framework's container:

```bash
cd tensorflow  # or pytorch, scikit, etc.
docker build -t hello-tensorflow .
docker run --rm hello-tensorflow -e IEXEC_OUT=/iexec_out -v ./iexec_out:/iexec_out  
```

For frameworks with `sconify.sh`, you can attempt to prepare the image for SCONE/SGX:

```bash
# Please edit the docker image name in the sconify.sh file beforehand

./sconify.sh  # ⚠️ May not work due to SGX limitations
```

---

## 📌 Notes

- Python 3 is used in all images
- Designed for experimentation and integration in confidential computing pipelines
- All containers are based on compatible and minimal Linux images to ensure reproducibility and compatibility with Intel TDX. The following base images are used across different frameworks:
	•	ubuntu:20.04 for general compatibility and system package support
	•	Official runtime base images (e.g., openvino/ubuntu20_runtime)
	•	python:3.9-bullseye for compatibility with SCONE and Intel SGX tooling

	⚠️ Some frameworks include sconify.sh scripts for SGX compatibility, but execution may not succeed on SGX for openvino, scikit, and numpy due to runtime limitations.

---

## 📬 Contributing

Feel free to open issues or PRs to add:
- More frameworks (e.g., ONNX, XGBoost)
- SGX fixes
- Extended examples

