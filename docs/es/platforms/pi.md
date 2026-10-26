# pi

*Última revisión: 2026-10-26 (contra la propia documentación de pi: páginas de configuración, seguridad y CLI).*

**Dónde va la carta:** `AGENTS.md` (o `CLAUDE.md`) en la carpeta donde ejecutas pi. pi carga esos **archivos de contexto** desde su directorio de agente, el directorio de trabajo y sus **directorios superiores**.

## Pasos

1. **Crea una carpeta nueva y vacía** para este agente, en un lugar cuyas carpetas superiores no tengan `AGENTS.md` / `CLAUDE.md` propios (o ejecuta una vez con `--no-context-files` para ver la diferencia).
2. Guarda la carta como `AGENTS.md` en esa carpeta.
3. Ejecuta `pi` desde esa carpeta. Saluda. Espera preguntas, no trabajo.
4. Responde; lee y confirma el SOUL. El agente escribe `SOUL.md` en la carpeta.
5. Agrega al final de `AGENTS.md`: «Al comienzo de cada sesión, lee SOUL.md en esta carpeta y síguelo». Tras editar archivos de contexto, `/reload` los carga sin reiniciar.

## Otros dos lugares, y cuándo usarlos

| Archivo | Efecto | Úsalo cuando |
| --- | --- | --- |
| `.pi/APPEND_SYSTEM.md` | Agrega tu texto al prompt de sistema de pi | Quieres la carta a nivel de sistema y no como archivo de contexto. Requiere que el proyecto sea de confianza. |
| `.pi/SYSTEM.md` | **Reemplaza** el prompt de sistema por defecto de pi | Rara vez. Pierdes la guía de herramientas propia de pi. |
| `<agent-dir>/AGENTS.md` | Vale en *toda* carpeta donde ejecutes pi | **No para esto.** La carta llegaría a todos tus proyectos. |

## Dónde vive el SOUL

`SOUL.md` en la carpeta del agente.

## Límites y cuidados

- **Los archivos de contexto se cargan sin importar la confianza del proyecto.** Las notas de seguridad de pi dicen que hay que tratar las instrucciones de una carpeta como entrada no confiable. Usa solo una carta que hayas leído tú.
- pi tiene herramientas de archivos y shell con los permisos de tu sistema operativo. La carta pide al agente que espere; lo que lo detiene son los permisos y tu atención. Para los primeros arranques usa una carpeta separada (o un contenedor) sin nada valioso.
- También se cargan archivos de directorios superiores, así que un `AGENTS.md` superior puede cambiar el comportamiento del agente.

## Fuente

Comprobado el 2026-10-26 contra la documentación incluida en pi 1.4 (las páginas *configuration*, *security* y *CLI*). Es la fuente para tu versión: los nombres de archivo, el orden de carga y las reglas de confianza pueden cambiar entre versiones.
