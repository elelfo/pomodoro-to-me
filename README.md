# 🍅 Pomodoro Timer

Una aplicación de escritorio moderna y minimalista para aplicar la técnica Pomodoro y mejorar tu productividad. Construida con Python y Tkinter.

![Python](https://img.shields.io/badge/Python-3.7+-3776ab?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=flat-square)

## 📋 Características

- ⏱️ **Temporizador configurable** - Personaliza los tiempos de trabajo y descanso
- 🔊 **Notificaciones sonoras** - Alarmas al finalizar cada sesión
- 📊 **Barra de progreso visual** - Visualiza el avance en tiempo real
- ⏸️ **Controles intuitivos** - Pausar, reanudar y resetear sesiones
- 🎯 **Ajuste rápido de tiempo** - Suma o resta minutos sobre la marcha
- ⚙️ **Configuración desplegable** - Panel de ajustes limpio y ordenado
- 📈 **Contador de sesiones** - Sigue tu progreso diario
- 🎨 **Interfaz minimalista** - Diseño oscuro moderno y accesible
- 📝 **Código documentado** - Docstrings PEP 257 en todo el proyecto

## 🚀 Inicio Rápido

### Requisitos
- Python 3.7 o superior
- Tkinter (incluido por defecto en Python en Windows y macOS)

### En Linux (si es necesario):
```bash
# Debian/Ubuntu
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/elelfo/pomodoro-to-me.git
cd pomodoro-to-me

# Ejecutar la aplicación
python pomodoro.py
```

## 💡 Cómo Usar

1. **Iniciar sesión**: Haz clic en el botón "▶ Iniciar"
2. **Trabajar**: Trabaja durante el tiempo configurado (default: 25 minutos)
3. **Descansar**: Toma un descanso cuando suene la alarma
4. **Repetir**: La aplicación alterna automáticamente entre trabajo y descanso

### Botones de Control
- **▶ Iniciar**: Comienza el temporizador
- **⏸ Pausa**: Pausa la sesión actual
- **🔄 Reset**: Reinicia todo a los valores por defecto

### Ajuste de Tiempo
- **➖ -1 min / ➖ -5 min**: Resta tiempo (solo cuando está pausado)
- **➕ +1 min / ➕ +5 min**: Suma tiempo (solo cuando está pausado)

### Configuración
- Haz clic en "⚙️ Configuración" para expandir el panel
- Personaliza tiempos de trabajo, descanso corto y descanso largo
- Guarda los cambios con "💾 Guardar configuración"

## 📐 Técnica Pomodoro

La técnica Pomodoro es un método de gestión del tiempo que divide el trabajo en intervalos focalizados:

1. **Trabajo**: 25 minutos de concentración total
2. **Descanso corto**: 5 minutos para recuperarte
3. **Ciclo**: Después de 4 ciclos, toma un descanso largo de 15 minutos

Esta aplicación implementa automáticamente estos intervalos.

## 🔧 Estructura del Proyecto

```
pomodoro-timer/
├── pomodoro.py          # Archivo principal
├── README.md            # Este archivo
├── LICENSE              # Licencia MIT
└── .gitignore          # Archivos ignorados por Git
```

## 📚 Documentación del Código

El código sigue las convenciones **PEP 257** para documentación:

```python
def nombre_funcion(parametro: tipo) -> tipo_retorno:
    """
    Descripción breve de qué hace la función.

    Descripción más detallada si es necesario.

    Args:
        parametro: Descripción del parámetro

    Returns:
        Descripción del valor retornado

    Raises:
        Excepción: Cuándo se lanza la excepción
    """
```

## 🛠️ Desarrollo

### Requisitos de desarrollo
```bash
# No se requieren dependencias externas
# Solo Python 3.7+
```

### Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añade nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 🐛 Reportar Bugs

Si encuentras un error, por favor:

1. Verifica que el error no está ya reportado
2. Crea un issue nuevo con:
   - Descripción clara del problema
   - Pasos para reproducirlo
   - Tu sistema operativo y versión de Python
   - Screenshots si es relevante

## 📝 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

### Licencias de Dependencias

El proyecto usa las siguientes librerías de Python con licencias compatibles:

| Librería | Versión | Licencia | Compatibilidad |
|----------|---------|---------|-----------------|
| tkinter | Built-in | PSF/BSD | ✅ Compatible |
| threading | Built-in | PSF | ✅ Compatible |
| winsound | Built-in | PSF | ✅ Compatible |

Todas las dependencias son parte de la librería estándar de Python y están bajo licencias compatibles con MIT.

## ⚖️ Términos de Uso

Este software se proporciona "tal cual", sin garantías de ningún tipo. Los autores no son responsables de ningún daño directo, indirecto, incidental, especial, ejemplar o derivado del uso de este software.

## 🙏 Agradecimientos

- Inspirado por la [Técnica Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) de Francesco Cirillo
- Construido con [Python](https://www.python.org/) y [Tkinter](https://docs.python.org/3/library/tkinter.html)

## 📞 Contacto

- **Issues**: [GitHub Issues](https://github.com/elelfo/pomodoro-to-me/issues)
- **Discussions**: [GitHub Discussions](https://github.com/elelfo/pomodoro-to-me/discussions)
- **Repository**: [github.com/elelfo/pomodoro-to-me](https://github.com/elelfo/pomodoro-to-me)

## 📊 Estado del Proyecto

- ✅ Versión: 1.0.0
- ✅ Estado: Estable
- ✅ Mantenimiento: Activo

---

**Hecho con ❤️ en Python**
