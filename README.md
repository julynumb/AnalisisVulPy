# SCRIPT PARA FILTRAR POR GRUPO EL ARCHIVO DE VULNERABILIDADES

### **Esta escrito en python.**

### **Utiliza virtual environment.**

### **Para utilizarlo se coloca en excel a analizar en la carpeta "FilesToProcess"**
```
ORIGIN_DIR = "./FilesToProcess"
```
### Los resultados una vez procesados seran colocados en la carpeta "FilesByGroup"
```
DESTINY_DIR = "./FilesByGroup"
```

###En el primer valor de la lista "VALUES_FF", se coloca el nombre del grupo
```
VALUES_FF = ["angier", "VULNERABLE", "Untreated"]
```