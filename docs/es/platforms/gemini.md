# Gemini (Gems y Gemini CLI)

*Última revisión: 2026-10-26.*

Dos productos distintos, dos formas distintas.

## Gemini Gems (aplicación de chat)

**Dónde va la carta:** el campo **Instrucciones** del Gem.

1. Crea un **Gem nuevo** con el nombre de trabajo del agente.
2. Pega la **carta completa** en Instrucciones. Si no cabe, usa la alternativa de aviso más archivo descrita en la [página de ChatGPT](chatgpt.md#alternativa-cuando-la-carta-es-más-larga-que-el-campo) (adjunta la carta como archivo de conocimiento del Gem).
3. Abre el Gem, saluda, responde las preguntas, lee y confirma el SOUL.
4. **Guarda el SOUL a mano**: un Gem no puede escribir archivos. Agrega el texto del SOUL a las Instrucciones del Gem debajo de la carta, o adjúntalo como archivo de conocimiento y di en las instrucciones que lo lea primero.

Cuidados: los Gems no tienen herramientas propias salvo que las conectes; mantén apagadas las apps conectadas hasta que el SOUL declare una necesidad. Revisa la configuración de compartir: mantén el Gem privado.

## Gemini CLI

**Dónde va la carta:** un archivo de contexto `GEMINI.md` en la carpeta donde ejecutas el CLI.

1. **Crea una carpeta vacía**, guarda la carta como `GEMINI.md` y ejecuta el CLI ahí con `--approval-mode default` o `plan` (no `auto_edit` ni `yolo`).
2. Cuando confirmes el SOUL, el agente escribe `SOUL.md`; agrega una línea al final de `GEMINI.md`: «Al comienzo de cada sesión, lee SOUL.md en esta carpeta y síguelo».
3. Como otros agentes basados en carpeta, también carga archivos de contexto de carpetas superiores: mantén la carpeta aislada.

## Confirmado en la documentación oficial (consultada el 2026-10-26)

| Dato | Fuente |
| --- | --- |
| **Modos de aprobación de Gemini CLI** (flag `--approval-mode`): `default` (pide para la mayoría de las escrituras), `auto_edit` (autoaprueba algunas escrituras; en archivos de política se llama `autoEdit`), `yolo` (autoaprueba herramientas: úsalo con extrema cautela), `plan` (solo lectura, definido por política). El motor de políticas (allow / deny / ask_user, prioridades, reglas de administrador) sigue importando. **Un modo no es aislamiento del sistema operativo ni autorización de tu organización.** | [Policy engine](https://geminicli.com/docs/reference/policy-engine/), [Referencia del CLI](https://geminicli.com/docs/cli/cli-reference/) |

## No documentado — compruébalo tú

- **Un largo máximo para las instrucciones de un Gem** no está publicado en las páginas oficiales de Gems consultadas ([guías de Gems](https://support.google.com/gemini/answer/15236321?hl=en), [instrucciones de un Gem](https://support.google.com/gemini/answer/15235603?hl=en)): dan una estructura, no una cifra. No tomes prestados límites de la API de Gemini (`systemInstruction`) ni de los tamaños de contexto de los modelos.
- Si los Gems conservan memoria entre conversaciones y el orden de carga de archivos de contexto del CLI: revisa la documentación del producto para tu versión.

Lista completa de fuentes y salvedades: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
