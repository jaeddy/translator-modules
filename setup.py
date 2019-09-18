# First, we try to use setuptools. If it's not available locally,
# we fall back on ez_setup.
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

long_description = ''

install_requires = []
with open('requirements.txt') as requirements_file:
    for line in requirements_file:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        pinned_version = line.split()[0]
        install_requires.append(pinned_version)

setup(
    name='translator-modules',
    description='NCATS Translator Reasoner modules',
    packages=find_packages(),
    url='https://github.com/ncats/translator-modules',
    download_url='https://github.com/ncats/translator-modules',
    entry_points={
        'console_scripts': [
            'tissue_to_tissue_bicluster = translator_modules.anatomical_entity.anatomical_entity.tissue_to_tissue_bicluster:main',
            'tissue_to_gene_bicluster = translator_modules.anatomical_entity.gene.tissue_to_gene_bicluster:main',
            'disease_associated_genes = translator_modules.disease.gene.disease_associated_genes:main',
            'disease_to_phenotype_bicluster = translator_modules.disease.phenotypic_feature.disease_to_phenotype_bicluster:main',
            'gene_to_tissue_bicluster = translator_modules.gene.anatomical_entity.gene_to_tissue_bicluster:main',
            'gene_to_cell_line_bicluster_DepMap = translator_modules.gene.cell_line.gene_to_cell_line_bicluster_DepMap:main',
            'chemical_gene_interaction = translator_modules.gene.chemical_substance.chemical_gene_interaction:main',
            'functional_similarity = translator_modules.gene.gene.functional_similarity:main',
            'phenotype_similarity = translator_modules.gene.gene.phenotype_similarity:main',
            'gene_interaction=translator_modules.gene.gene.gene_interaction:main',
            'gene_to_gene_bicluster_RNAseqDB = translator_modules.gene.gene.gene_to_gene_bicluster_RNAseqDB:main',
            'gene_to_gene_bicluster_DepMap = translator_modules.gene.gene.gene_to_gene_bicluster_DepMap:main',
            'phenotype_to_disease_bicluster = translator_modules.phenotypic_feature.disease.phenotype_to_disease_bicluster:main',
        ]
    },
    long_description=long_description,
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov', 'mock'],
    license='Apache 2.0',
    zip_safe=False,
    author='James Eddy',
    author_email='james.a.eddy@gmail.com',
    version='0.2.0'
)