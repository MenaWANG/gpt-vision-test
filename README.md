
## 📸 GPT Vision Quick Demo and Test
This repo serves as a quick demonstration and test of document recognition using the GPT-4 model. In this demo, we'll explore how GPT-4 can be used to analyze and interpret various types of documents, such as receipts, invoices, forms, and more. All the images/docuemnts in the repo are dummy ones found online or created for testing purposes only.

## 📄 More on Document Recognition
Document recognition, also known as document analysis or document understanding, is the process of extracting useful information from documents in various formats, including images, PDFs, and scanned documents. It involves tasks such as text extraction, entity recognition, key information extraction, and document classification.

## 🚀 How to Use
You'll need to 
* have the necessary dependencies installed (pls see `requirements_py311.txt`).  [Link](https://github.com/MenaWANG/venv_test) to a quick demo of python virtual environment.  
* Save the below credentials in your `.env` file and ensure `.env` is in your `.gitignore`. [More info](https://pypi.org/project/python-dotenv/) on {dotenv}📦 for secrete management.  
    * Azure Resources:
        * `AZURE_ENDPOINT` & `AZURE_API_KEY`: Go to Azure AI Studio, deploy a GPT-vision model, go to playground and click `code`, find `curl` and get URL from there. It will look something like `f"https://{RESOURCE_NAME}.openai.azure.com/openai/deployments/{DEPLOYMENT_NAME}/extensions/chat/completions?api-version=2023-12-01-preview"`
    * OpenAI Resources:
        * `OPENAI_API_KEY`: https://platform.openai.com/api-keys 


## 📚 Reference:
* [Quick start with vision](https://platform.openai.com/docs/guides/vision) 
* [Use GPT-4 Turbo with vision](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/gpt-with-vision?tabs=rest%2Csystem-assigned%2Cresource)
