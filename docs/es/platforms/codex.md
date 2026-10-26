# Codex (OpenAI Codex CLI)

*Última revisión: 2026-10-26.*

**Dónde va la carta:** un archivo `AGENTS.md` en la carpeta donde ejecutas Codex. Codex lee los archivos de instrucciones al empezar la sesión; existe también uno a nivel de usuario, pero no es el lugar para esto.

## Pasos

1. **Crea una carpeta nueva y vacía** para este agente.
2. Guarda la carta como `AGENTS.md` en esa carpeta.
3. Inicia Codex desde esa carpeta con el **sandbox `read-only`** y `approval_policy = on-request` (usa `/permissions` para revisarlos o cambiarlos). Saluda.
4. Espera preguntas, no trabajo. Responde, lee el SOUL que propone el agente, corrígelo y confirma.
5. El agente escribe `SOUL.md` junto a `AGENTS.md`. Como los archivos de instrucciones pueden no importarse entre sí, agrega al final de `AGENTS.md`:

```text
Al comienzo de cada sesión, lee SOUL.md en esta carpeta y síguelo.
```

## Dónde vive el SOUL

`SOUL.md` en la carpeta del agente.

## Límites y cuidados

- Los archivos de instrucciones se combinan bajo un **presupuesto de 32 KiB (32.768 bytes) por defecto**, compartido por toda la cadena descubierta. La carta de agente solo pesa unos 9 KB y la de líder unos 13,7 KB (UTF-8, ver [tamaños](README.md#qué-tan-largas-son-las-cartas)), así que caben solas; pero un `AGENTS.md` global más archivos de carpetas superiores cuentan contra el mismo presupuesto, y Codex deja de agregar archivos al alcanzar el tope. Mantén la carpeta aislada y comprueba, en la primera respuesta, que el agente sigue el protocolo hasta el final.
- Codex es un agente de programación con herramientas de shell y archivos. Lo que realmente lo frena es el **modo de aprobación**; la carta solo pide.
- `~/.codex/AGENTS.md` (a nivel de usuario) vale en todas partes. No pongas la carta ahí.

## Confirmado en la documentación oficial (consultada el 2026-10-26)

| Dato | Fuente |
| --- | --- |
| **Tope de tamaño:** 32 KiB = 32.768 **bytes** por defecto, configurable con `project_doc_max_bytes`. Es un presupuesto *combinado* de la cadena descubierta, no caracteres ni una cuota por archivo. | [Guía de AGENTS.md](https://developers.openai.com/codex/guides/agents-md) |
| **Descubrimiento y fusión:** primero el archivo global (`AGENTS.override.md`, si no `AGENTS.md`, el primero no vacío); luego desde la raíz del proyecto hasta el directorio de trabajo, **como máximo un archivo por directorio**, concatenados con líneas en blanco, las instrucciones más cercanas al final. Si no se halla raíz de proyecto, solo el directorio de trabajo. Se construye al inicio de cada ejecución o sesión. | [Guía de AGENTS.md](https://developers.openai.com/codex/guides/agents-md) |
| **Política de aprobación:** `on-request`, `never` o un objeto granular. `untrusted` no está soportado y `on-failure` está en desuso. (No confundir el `approval_policy = untrusted` retirado con `projects.<ruta>.trust_level = untrusted`, que sigue documentado.) | [Referencia de configuración](https://developers.openai.com/codex/config-reference), [Aprobaciones y seguridad](https://developers.openai.com/codex/agent-approvals-security) |
| **Sandbox:** `read-only`, `workspace-write`, `danger-full-access`. Son independientes de la política de aprobación: `never` quita los avisos pero **no** concede acceso total ni elimina el sandbox. El acceso total/bypass no se recomienda aquí. | las mismas dos páginas |

Lista completa de fuentes y salvedades: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
