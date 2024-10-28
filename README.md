# CVAT-Setup-Directory-Helper
So I made this repo because, I have difficulty managing the number of frames extracted from CVAT (Computer Vision Annotation Tool), which when the input is Video, the default frame taken is 30 fps (probably?), while what is needed is not always that much, and also related to splitting data, I don't think CVAT has that feature yet, so that's why I made this repo.

# How to run?

## **Step 1 Clone the repository in your working directory**
```bash
git clone https://github.com/AnggaDS01/CVAT-Setup-Directory-Helper.git
```

```bash
cd CVAT-Setup-Directory-Helper
```

## **Step 2 Create a virtual environment after opening the repository**
Here I am using python version 3.11.10, make sure the python version you are using is 3.10+, in creating a virtual environment you can use [Anaconda](https://www.anaconda.com/download/success) or [Miniconda](https://docs.anaconda.com/miniconda/), here I use Miniconda version 24.9.2, to create it you can type the following command:

### **Step 2.1 Create a virtual environment using the conda prompt**
```bash
# conda create -n <directory_name> python=<python_version> ipython
conda create -n "myenv" python=3.11.10 ipython
```

#### **Step 2.1.1 Activate the virtual environment**

```bash
# To activate this environment, use
#
#     $ conda activate myenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

when you attempt to type the command `conda activate myenv`

```bash 
conda activate myenv
```

and get an error like this:

Output:
```bash
CondaError: Run 'conda init' before 'conda activate'
```

> **Note: Please restart your shell and open it again in your shell, then your conda will be activated.**

### **Step 2.2 Create a virtual environment using the venv module**
```bash
# python -m venv <directory>
python -m venv myenv
```

#### **Step 2.2.1 Windows venv activation**
To activate your venv on Windows, you need to run a script that gets installed by venv. If you created your venv in a directory called `myvenv`, the command would be:

```bash
# In cmd.exe
myenv\Scripts\activate.bat
# In PowerShell
myenv\Scripts\Activate.ps1
```

#### **Step 2.2.2 Linux and MacOS venv activation**
On Linux and MacOS, we activate our virtual environment with the source command. If you created your venv in the `myvenv` directory, the command would be:

```bash
$ source myvenv/bin/activate
```

## **Step 3 Install the requirements**

```bash
pip install -r requirements.txt
```

## **Step 4 How the program works**
Structure folder:

```
CVAT-Setup-Directory-Helper
├── .gitignore
├── annotation_tool_helper.egg-info
├── control_panel.py
├── Data Zone
│   ├── Annotated-Images-Assets [IF YOU HAVE IMAGES PUT THEM HERE]
│   │   ├── Highway-Traffic [OUTPUT FOR VIDEO CASE]
│   │   │   └── HT_00001
|   |   |       ├── data_train
|   |   |       |   ├── images
|   |   |       |   |   ├── HT_00001_00000.jpg
|   |   |       |   |   ├── HT_00001_00003.jpg
|   |   |       |   |   ├── ...
|   |   |       |   └── labels
|   |   |       |   |   ├── HT_00001_00000.txt
|   |   |       |   |   ├── HT_00001_00003.txt
|   |   |       |   |   ├── ...
|   |   |       ├── data_test
|   |   |       └── data_valid
│   │   └── Highway-Traffic-02 [LET'S SAY YOU PUT YOUR PICTURES IN THIS FOLDER]
|   |   |   ├── HT_00001_00000.jpg
|   |   |   ├── HT_00001_00001.jpg
|   |   |   ├── ...
│   └── Videos-Assets [IF YOU HAVE A VIDEO PUT IT HERE]
│       └── Highway-Traffic
│           └── HT_00001
|               └── 4K Video of Highway Traffic! (online-video-cutter.com).mp4
├── demo.py
├── main.txt
├── notebook
│   └── experiments.ipynb
├── README.md
├── requirements.txt
├── run_pipeline.py
├── run_plot_results.py
├── setup.py
├── src
│   ├── components
│   │   ├── coco_src
│   │   │   ├── coco_setup_directory_structure.py
│   │   │   └── coco_splitter.py
│   │   ├── display_function_name.py
│   │   ├── get_file_list.py
│   │   ├── pascal_voc_src
│   │   │   ├── pascal_voc_setup_directory_structure.py
│   │   │   └── pascal_voc_splitter.py
│   │   ├── plot_results
│   │   │   ├── plot_coco_json_bbox.py
│   │   │   ├── plot_pascal_voc_bbox.py
│   │   │   └── plot_yolo_bbox.py
│   │   ├── setup_images_directory.py
│   │   ├── split_helper.py
│   │   ├── target_store_directory.py
│   │   ├── video_to_frames.py
│   │   └── yolo_src
│   │       ├── yolo_setup_directory_structure.py
│   │       ├── yolo_setup_labels_directory.py
│   │       └── yolo_splitter.py
│   ├── constants
│   │   └── __init__.py
│   ├── pipeline
│       ├── coco_pipeline.py
│       ├── cvat_setup_directory_pipeline.py
│       ├── pacal_voc_pipeline.py
│       └── yolo_pipeline.py
├── tree.py
└── tree_output.txt
```