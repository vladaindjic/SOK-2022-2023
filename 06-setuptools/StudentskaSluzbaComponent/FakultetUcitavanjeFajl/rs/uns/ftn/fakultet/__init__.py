# Potrebno zbog namespace_pakages
# parametra u setup.py modulu
# Ovaj deo koda je potreban da bi paket bio prijavljen
# kao namespace.

__import__('pkg_resources').declare_namespace(__name__)