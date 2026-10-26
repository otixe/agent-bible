# Plataformas: dónde va la carta

Casi toda plataforma de agentes tiene los mismos pocos lugares para configurar un agente, con nombres distintos. Busca el que guarda **instrucciones que valen para toda conversación**: ahí va la carta.

| Este manual dice | Nombres habituales en las plataformas |
| --- | --- |
| **Instrucciones** (aquí va la carta) | «instrucciones», «prompt de sistema», «instrucciones del proyecto», «persona», «archivo de contexto», «reglas» |
| **Conocimiento** | «conocimiento», «archivos», «documentos», «conocimiento del proyecto», «documentos de referencia» |
| **Herramientas / acciones** | «herramientas», «acciones», «conectores», «plugins», «integraciones», «servidores MCP» |
| **Compartir / permisos** | «compartir», «acceso», «roles», «modo de aprobación», «sandbox» |
| **Memoria** | «memoria», «contexto persistente»; si no hay, un documento que mantienes tú |

## De un vistazo

*Última revisión: 2026-10-26. Cada página termina con lo que se **confirmó en la documentación oficial** (con enlaces) y lo que **no está documentado**. «No documentado» significa sin cifra publicada, no ilimitado. Evidencia y salvedades: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).*

| Plataforma | Dónde va la carta | ¿El agente puede guardar su SOUL? | Cuidado principal |
| --- | --- | --- | --- |
| [Claude Projects](claude-projects.md) | Instrucciones del proyecto | No: lo guardas tú | El tope de instrucciones no está documentado; una versión beta nueva se despliega de forma selectiva |
| [ChatGPT](chatgpt.md) | Instrucciones del proyecto, o el campo Instrucciones de un GPT | No: lo guardas tú | Las Custom Instructions de toda la cuenta son demasiado chicas (1.500–5.000 caracteres); los topes de proyecto y GPT no están documentados |
| [Claude Code](claude-code.md) | `CLAUDE.md` en una carpeta vacía | Sí, como archivo | El agente tiene herramientas de archivos y shell: empieza en modo `default` o `plan`; un modo no es un sandbox |
| [Codex](codex.md) | `AGENTS.md` en una carpeta vacía | Sí, como archivo | Presupuesto combinado de 32 KiB para los archivos de instrucciones; sandbox y aprobación son controles separados |
| [pi](pi.md) | `AGENTS.md` (o `.pi/APPEND_SYSTEM.md`) en una carpeta vacía | Sí, como archivo | También se cargan los archivos de contexto de carpetas superiores |
| [Gemini](gemini.md) | «Instrucciones» de un Gem; `GEMINI.md` en el CLI | Gem: no. CLI: sí | Los Gems no escriben archivos; guarda el SOUL como texto |
| [Amazon Quick](amazon-quick.md) | Perfil del agente → Instrucciones | No: lo guardas tú | El tope de las instrucciones no está documentado (las 100.000 son para documentos subidos); omite la plantilla «generar» |
| [Otras herramientas](other-tools.md) | Archivo de reglas/instrucciones o prompt de sistema | Depende | Revisa las ocho preguntas de abajo |
| Nada encaja | Primer mensaje de una conversación nueva | No: lo guardas tú | Solo vale para esa conversación |

## ¿Qué tan largas son las cartas?

Medido sobre los archivos de este repositorio (caracteres Unicode incluyendo saltos de línea; los bytes son UTF-8; **no son tokens**). Fuente: [`evidencia/sizes.json`](../../../evidencia/sizes.json).

| Carta | Caracteres | Bytes |
| --- | ---: | ---: |
| [Agente solo, español](../../../carta/es/CARTA-AGENTE-SOLO.md) | 8.959 | 9.115 |
| [Agente solo, inglés](../../../carta/en/LETTER-SOLO-AGENT.md) | 8.543 | 8.577 |
| [Líder de equipo, español](../../../carta/es/CARTA-LIDER-DE-EQUIPO.md) | 13.510 | 13.721 |
| [Líder de equipo, inglés](../../../carta/en/LETTER-TEAM-LEAD.md) | 13.201 | 13.227 |

**Todas las cartas superan los 8.000 caracteres.** No supongas que caben en un campo de instrucciones corto y no la recortes para que quepa: una carta sin algunas reglas o sin el protocolo de primer arranque es otro texto, no probado. Si un campo tiene un tope menor que el tamaño de la carta, usa una de las [alternativas](chatgpt.md#alternativa-cuando-la-carta-es-más-larga-que-el-campo): la carta completa como archivo adjunto con un aviso corto en las instrucciones, o la carta completa como primer mensaje de una conversación. En ambos casos comprueba en la primera respuesta que el agente realmente empezó con las preguntas. Las reglas y el Harness por sí solos son pequeños ([reglas](../../../reglas/es/REGLAS-DE-ORO.md) ≈ 3.000 caracteres, [Harness de agente solo](../../../harness/es/HARNESS-AGENTE-SOLO.md) ≈ 3.200) si quieres adjuntarlos aparte.

## Dos familias, dos formas de conservar el SOUL

**Plataformas de chat** (Claude Projects, ChatGPT, Gemini Gems, Quick). El agente no puede escribir archivos. Al final del primer arranque *imprime* su SOUL; tú lo guardas pegándolo en las instrucciones de la plataforma (bajo la carta) o subiéndolo como archivo de conocimiento, como explica cada página. Si no lo haces, la siguiente conversación empieza sin saber quién es el agente.

**Agentes basados en carpeta** (Claude Code, Codex, pi, Gemini CLI). El agente corre en una carpeta y, si permites escribir archivos y nombras el lugar en la pregunta 4, guarda `SOUL.md` ahí (nunca en un sitio inventado; no sobrescribe archivos anteriores). La carta vive en el archivo de instrucciones de la carpeta; desde la segunda sesión el agente lee su SOUL al empezar. **Usa una carpeta vacía dedicada a este agente**: no un repositorio de código, ni una carpeta dentro de otra que ya tenga sus propios archivos de instrucciones.

## Ocho preguntas antes de elegir o configurar una plataforma

| Pregunta | Por qué importa |
| --- | --- |
| ¿Dónde se procesan y almacenan los datos, y por cuánto tiempo? | Las normas de privacidad aplican a lo que le muestras al agente. |
| ¿Se usan las conversaciones o archivos para entrenar modelos del proveedor? ¿Se puede desactivar? | Confidencialidad. |
| ¿Puedes limitar fuentes y acciones por agente? | Mínimo privilegio (Regla de Oro 5). |
| ¿Las acciones con efecto piden tu confirmación antes de ejecutarse? | Reglas 1 y 2. Si no, la *carta* debe exigirla y tú debes probarlo. |
| ¿Hay un registro de actividad que puedas leer? | Trazabilidad (Regla 8). |
| ¿Cuál es el largo máximo de las instrucciones? | Define si la carta cabe o necesita la alternativa. |
| ¿Hay memoria persistente, y puedes verla y borrarla? | Aprendizaje controlado. |
| ¿Se integra con el inicio de sesión de tu organización? | Para que el humano del agente sea quien dice ser. |

## Reglas de configuración que valen en todas partes

1. **Habilita solo lo que el SOUL declara.** Cada fuente y cada acción debe corresponder a una función escrita en el SOUL.
2. **Empieza en modo lectura.** Activa las acciones con efecto de a una, después de probarlas.
3. **No compartas el agente** más allá de su humano responsable sin una nueva decisión.
4. **Anota la configuración que aplicaste**, para compararla con el SOUL más tarde.
5. **Si la plataforma no ofrece un control**, por ejemplo la confirmación antes de una acción, ese control se escribe en el SOUL y se prueba. Su ausencia no elimina la regla.
6. **Si la carta no cabe**, conserva en este orden: Reglas de Oro, identidad y límites, Harness, estilo. Los ejemplos y el detalle van en un documento adjunto.
