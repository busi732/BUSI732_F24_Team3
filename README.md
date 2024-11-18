# 🚩BUSI732 Fall2024 Team3


## 📚Table of Contents
1. [Getting Started](#getting-started)
2. [Setting Up the Environment](#setting-up-the-environment)
3. [Selecting the Conda Environment in VS Code](#selecting-the-conda-environment-in-vs-code)
4. [Running the Project](#running-the-project)
5. [Contributing to the Project](#contributing-to-the-project)
6. [Project Structure](#project-structure)

---

### 💡Getting Started

1. **Clone the Repository**:
   - Open Visual Studio Code, then open the terminal by going to **View > Terminal** or pressing `Ctrl + ` ` (backtick).
   - Clone the repository by running the following commands:
     ```bash
     git clone https://github.com/busi732/BUSI732_F24_Team3.git
     cd BUSI732_F24_Team3
     ```

### Setting Up the Environment

The project uses Conda for managing dependencies. You’ll set up the environment using the `environment.yml` file, which includes all required packages.

1. **Create the Conda Environment**:
   - Run the following command in the terminal to create the environment:
     ```bash
     conda env create -f environment.yml
     ```
   - This command will create a new Conda environment called `wind_turbine_env` with the dependencies listed in `environment.yml`.

2. **Activate the Environment**:
   - After creating the environment, activate it with:
     ```bash
     conda activate fu24_block2_team3_env
     ```

3. **Add the Environment to Jupyter**:
   - To ensure that the environment is available as a kernel in Jupyter notebooks, run:
     ```bash
     python -m ipykernel install --user --name=fu24_block2_team3_env --display-name "Python (fu24_block2_team3_env)"
     ```

### Selecting the Conda Environment in VS Code

After setting up the Conda environment, follow these steps to select it in VS Code:

1. **Open a Jupyter Notebook**:
   - In VS Code, navigate to `notebooks/mytests/check_conda.ipynb` or any other notebook in the project.

2. **Open the Kernel Selector**:
   - At the top right of the notebook, you’ll see a kernel selector (or a prompt asking you to select a kernel). Click on it to open the environment selection dropdown.

3. **Choose the Correct Environment**:
   - In the list, look for `fu24_block2_team3_env` with the specified Python version (e.g., `Python 3.8.x`). It should appear under **Conda Env**.
   - Click on `fu24_block2_team3_env` to select it as the active environment for the notebook.

4. **Verify the Selection**:
   - Once selected, you should see "fu24_block2_team3_env (Python 3.8.x)" displayed at the top of the notebook. This confirms that the notebook is using the correct Conda environment.

### Running the Project

1. **Run Cells**:
   - Run individual cells in the notebook. Verify that each cell executes successfully to confirm that your environment is set up correctly.

### Contributing to the Project

To contribute, you may need to add new packages or update existing ones in the environment. Here’s how to do it:

1. **Add New Packages**:
   - If you need to add a new package, first install it into the environment with:
     ```bash
     conda install <package-name>
     ```
   - To update the `environment.yml` file with this change, export the current environment:
     ```bash
     conda env export --from-history > environment.yml
     ```
     > **Note**: `--from-history` includes only the packages you explicitly installed, which keeps `environment.yml` clean and avoids unnecessary dependencies.

     > ⚠️ **Important:** Please make sure the conda-forge is still under the channels section, if it is not, add it back to the first line under the channels section.
     
     > ⚠️ **Important:** Remove the last prefix line if it exists.

2. **Update Environment for Others**:
   - After updating `environment.yml`, other need to update their local environment to match the new configuration:
     ```bash
     conda env update --file environment.yml --prune
     ```
   - This will update their environment to match the `environment.yml` file, adding or removing packages as needed.

3. **Commit Your Changes**:
   - When you’ve made changes to the environment or code, commit and push them:
     ```bash
     git add .
     git commit -m "commit message"
     git push origin feature/your-branch-name
     ```
   - Consider opening a pull request (PR) for your contributions so they can be reviewed and merged.

---

### 🗃️Project Structure

This project follows a standard data science directory structure to keep code and data organized:

```plaintext
busi732/BUSI732_F24_Team3/
├── data/                   # Data files
│   ├── raw/                # Raw data files
│   ├── processed/          # Processed data
│   ├── external/           # External data sources
|   └── final/              # Data after training model
├── notebooks/              # Jupyter notebooks
│   └── mytests/            # Test notebooks
│       └── check_conda.ipynb   # A notebook for testing Conda setup
├── docs/                   # Documents
│   ├── references/         # References documents used
|   └── home.md             # Project wiki
├── src/                    # Source code scripts
├── models/                 # Serialized models and model checkpoints
├── reports/                # Generated analysis and reports
├── requirements.txt        # Dependencies for pip (optional)
├── environment.yml         # Conda environment configuration
└── README.md               # Project documentation
