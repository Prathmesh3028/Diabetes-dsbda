from setuptools import setup, find_packages

setup(
    name="diabetes-prediction-api",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask==2.0.2",
        "flask-cors==3.0.10",
        "scikit-learn==1.0.2",
        "pandas==1.3.5",
        "numpy==1.21.6",
        "joblib==1.1.0",
    ],
    python_requires=">=3.9,<3.10",
) 