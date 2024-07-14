



# Prompt Engineering with orca model

This repo contains the templates of several types of prompts that are applied on orca model.



## Prompt Engineering Guide:

Prompt engineering is a relatively new discipline for developing and optimizing prompts to efficiently use language models (LMs) for a wide variety of applications and research topics. Prompt engineering skills help to better understand the capabilities and limitations of large language models (LLMs). Researchers use prompt engineering to improve the capacity of LLMs on a wide range of common and complex tasks such as question answering and arithmetic reasoning. Developers use prompt engineering to design robust and effective prompting techniques that interface with LLMs and other tools.

Motivated by the high interest in developing with LLMs, we have created this new prompt engineering guide that contains all the latest papers, learning guides, lectures, references, and tools related to prompt engineering for LLMs.

Happy Prompting!

## Key Highlights

- Fine-tuned on complex explanation traces obtained from GPT-4
- Uses synthetic training dataset and Prompt Erasure technique
- Trained using a teacher-student scheme
- Outperforms models that are 10x larger
## Optimizations

- Orca models(3b/7b) is fed with blender shortcuts keys and tabulated the results 
- Changed the paramters to the default settings to obtain the results 
- Contents from "Air Solve Compliants xcel sheet" converted into Dictionary to train to model
-  The results from the models are Documented

# Software requirements


Starting an AI project involves several software requirements to develop, train, and deploy machine learning models. The specific requirements can vary depending on the nature of your project and the tools you choose, but here are some basic software requirements for an AI project:

**Python:**

Python is a widely used programming language in the field of AI and machine learning. Most AI frameworks and libraries are compatible with Python.

**Integrated Development Environment (IDE):**

Choose an IDE for coding and development. Popular choices include:
Jupyter Notebooks
PyCharm
Visual Studio Code

**Version Control:**

Use a version control system to track changes in your code. Git is the most commonly used version control system.

**Machine Learning Libraries and Frameworks:**

*TensorFlow

*PyTorch

*scikit-learn

**NumPy and pandas:**

NumPy for numerical operations and arrays.
pandas for data manipulation and analysis.

**Data Visualization:**

Matplotlib
Seaborn
Plotly



















# To run locally

Clone the project

```bash
  git clone https://git.dev.elgi.com/ELGi_DID/llm
```

Go to the project directory

```bash
  cd llm
```

Install requirements.txt file

```bash
  pip  install  requirements.txt
```

Start to execute






## Usage 

### use this snippet instead of requesting api key from openai

```javascript
import langchain.llms from Ollama

llm=Ollama(base_url='http://172.17.226.116:11434',
model="orca2:7b",temperature=0.8,top_k=40,top_p=0.9,repeat_penalty=1.1,repeat_last_n=64,tfs_z=1,
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))

```





## Documents to be read:

- **Parameter usage:** https://elgi-my.sharepoint.com/personal/intern_dx23_elgi_com/_layouts/15/Doc.aspx?sourcedoc=%7B6BB9FE2B-1B88-4006-8319-6224F5F4C7EE%7D&file=Parameters+Usage.pptx&action=edit&mobileredirect=true&DefaultItemOpen=1&login_hint=intern_dx23%40elgi.com&ct=1704714661161&wdOrigin=OFFICECOM-WEB.START.EDGEWORTH&cid=f36ffff4-17ac-4534-8efd-a8a75b91f039&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=5825c4ed-a574-4c9f-b3a5-7ef8e1fff42a

- **Comparision between orca models:**  https://elgi-my.sharepoint.com/personal/intern_dx23_elgi_com/_layouts/15/Doc.aspx?sourcedoc=%7BE7C8AEFF-00B3-4D40-8E95-30ACBA8F974B%7D&file=Manual+for+install+py+%26+code+for+llm.docx&action=default&mobileredirect=true&DefaultItemOpen=1&login_hint=intern_dx23%40elgi.com&ct=1704714741029&wdOrigin=OFFICECOM-WEB.START.REC&cid=48a1cbcf-dd43-429b-968b-ff48a6b19096&wdPreviousSessionSrc=HarmonyWeb&wdPreviousSession=5825c4ed-a574-4c9f-b3a5-7ef8e1fff42a

## Reference:

- https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/

- https://github.com/LinkedInLearning/advanced-prompt-engineering-techniques-3817061

- https://www.youtube.com/watch?v=CbpsDMwFG2g&list=PLZoTAELRMXVMTWGW9iS45ZTcMsntos6VO

- https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf




## 🛠 Github links
- https://github.com/krishnaik06/OPENAI-API-Tutorials

-  https://drp.li/nfMZY

