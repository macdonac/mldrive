import setuptools
setuptools.setup(
    name= "mldrive",
    version="1.0.7",
    author="mldrive",
    description='A Python wrapper for the MLdrive API. Functionality includes getting datasets, saving dataframes/models, loading dataframes/models, sending dataframes/models, recieving dataframes/models.',
  install_requires=[            
          'pandas',
          'requests',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True
)

