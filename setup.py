from setuptools import setup, find_packages

setup(
    name ="cycpred",
    packages = ["cycpred"],
    version = "1.0.0",
    python_requires='>3.8.0',
    install_requires=[
    "tensorflow==2.6.0",
    "keras==2.6.0",
    "scikit-learn==1.1.2",
    "numpy==1.19.5",
    "protobuf==3.20.*"],
    package_data = {"":["model/*"]},
    include_package_data=True,
    entry_points={"console_scripts":["cycpred = cycpred.exec_cycpred:main"]
    }
    )
    
    
