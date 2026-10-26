# ChatGPT

*Última revisión: 2026-10-26.*

Tienes tres lugares. Prefiere el primero. Ojo: el texto oficial indexado el 2026-10-26 indica que crear y publicar GPTs *nuevos* no está disponible en cuentas personales Free/Go/Plus/Pro, así que la ruta de GPT personalizado puede no estar abierta para ti.

| Ruta | Dónde va la carta | Sirve para | Problema |
| --- | --- | --- | --- |
| **Proyecto** | Las instrucciones del proyecto | Un agente persistente para trabajo continuo | El tope de las instrucciones del proyecto no está documentado: verifícalo en la primera respuesta |
| **GPT personalizado** | El campo *Instrucciones* del editor del GPT (pestaña Configurar) | Un agente que podrías compartir | Puede no estar disponible para crear en tu plan; el tope del campo no está documentado |
| **Un solo chat** | Primer mensaje | Una prueba | Nada persiste |

**No uses las «Custom Instructions» de toda la cuenta** para esto: valen para *todas* tus conversaciones, de cualquier tema, y harían que todo ChatGPT se comporte como este agente. Además son demasiado chicas para la carta: 1.500 caracteres en Free y Go, 5.000 en Plus, Pro, Enterprise, Business y Education ([fuente](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt)). Toda carta es más larga que eso.

## Pasos (proyecto)

1. Crea un **proyecto** con el nombre de trabajo del agente.
2. Pega la **carta completa** en las instrucciones del proyecto. Si el campo la rechaza, usa la alternativa de abajo.
3. Inicia un chat dentro del proyecto, saluda, responde las preguntas, lee y confirma el SOUL que imprime.
4. **Guarda el SOUL**: pégalo en las instrucciones del proyecto debajo de la carta, o súbelo como archivo del proyecto `SOUL.md` y agrega una línea a las instrucciones: «Al comienzo de cada conversación, lee SOUL.md y síguelo».

## Alternativa cuando la carta es más larga que el campo

1. Pon un **aviso corto** en Instrucciones: que las instrucciones completas de este agente están en el archivo adjunto `LETTER.md`, que debe leerlo entero antes de responder y que su primera respuesta debe ser las preguntas del primer arranque.
2. Sube la carta completa como archivo de conocimiento/proyecto llamado `LETTER.md`.
3. En tu primer chat, comprueba que el agente realmente empezó con las preguntas. Los archivos se recuperan, no siempre se cargan completos: si se salta el protocolo, pega la carta como primer mensaje.

## Particularidades del GPT personalizado

- Elige la configuración manual en vez de dejar que el constructor «genere» las instrucciones: el texto generado puede resumir o cambiar las reglas.
- Deja apagadas las **Acciones** y las herramientas de **navegación web / código** hasta que el SOUL las declare.
- Compartir un GPT comparte sus instrucciones con quien pueda abrirlo. Mantenlo privado.

## Límites y cuidados

- El agente no puede guardar archivos por ti; el SOUL lo conservas tú.
- La memoria propia de ChatGPT es una función aparte. Revisa qué recuerda.

## Confirmado en la documentación oficial (consultada el 2026-10-26)

| Dato | Fuente |
| --- | --- |
| **Custom Instructions** (de toda la cuenta): 1.500 caracteres en Free y Go; 5.000 en Plus, Pro, Enterprise, Business y Education. Go es un plan de pago pero se queda en 1.500. Esto **no** aplica a GPTs ni a Projects. | [Custom Instructions](https://help.openai.com/en/articles/8096356-custom-instructions-for-chatgpt), [notas de versión](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) |
| **Projects** está disponible en todos los tipos de suscripción, gratuitos y de pago, en todo el mundo. El plan y la administración cambian archivos, compartir y otras funciones; disponibilidad no significa cuotas iguales. | [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-chatgpt-projects) |

## No documentado — compruébalo tú

- **El límite de las instrucciones de un proyecto** y **del campo Instrucciones de un GPT** no están publicados en el texto oficial recuperado. La cifra de 8.000 caracteres que circuló para los GPTs es histórica: no te apoyes en ella. El artículo de ayuda que antes servía de guía para escribir instrucciones de GPTs ahora describe la disponibilidad de los GPTs.
- El acceso directo a las páginas de ayuda estuvo bloqueado (HTTP 403) durante la verificación, así que algunos datos se apoyan en el texto oficial indexado; eso no prueba que no exista un límite en otra parte de la documentación.

Lista completa de fuentes y salvedades: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
