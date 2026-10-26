# Claude Code

*Última revisión: 2026-10-26.*

**Dónde va la carta:** un archivo `CLAUDE.md` en la carpeta donde ejecutas el agente. Claude Code lo lee al empezar la sesión.

## Pasos

1. **Crea una carpeta nueva y vacía** para este agente (no un repositorio de código; no dentro de uno que ya tenga un `CLAUDE.md` más arriba).
2. Guarda la carta como `CLAUDE.md` en esa carpeta.
3. Inicia Claude Code desde esa carpeta en modo de permisos **`default` (también llamado Manual) o `plan`**, no en uno que apruebe automáticamente. Saluda.
4. Espera preguntas, no trabajo. Responde y luego lee el SOUL que propone el agente. Debe **mostrártelo antes de escribir el archivo**.
5. Al confirmar, el agente escribe `SOUL.md` en la misma carpeta. Agrega una línea al final de `CLAUDE.md` para que cada sesión posterior lo cargue:

```text
@SOUL.md
```

Escribe esa línea como texto plano **fuera de backticks o bloques de código** en tu `CLAUDE.md` real (aquí aparece en un bloque solo para explicarla; las importaciones no se expanden dentro de fragmentos de código ni bloques). La ruta es relativa al archivo que importa. Si tu versión no la expande, escribe en su lugar: «Al comienzo de cada sesión, lee SOUL.md y síguelo».

## Dónde vive el SOUL

`SOUL.md` en la carpeta del agente. Respáldalo como cualquier archivo; conserva la versión anterior cuando cambie.

## Límites y cuidados

- Claude Code es un **agente de programación** con herramientas de archivos y shell. La carta le dice que no actúe antes de las preguntas del primer arranque, pero solo el modo de permisos *impide* que escriba o ejecute cosas. Empieza con las aprobaciones activadas; afloja de a una.
- Un `~/.claude/CLAUDE.md` a nivel de usuario vale para todo proyecto que abras. **No** pongas la carta ahí.
- También se cargan los archivos de carpetas superiores; por eso la carpeta debe estar vacía y aislada.
- Las instrucciones de una carpeta son texto que el agente lee. No dejes una carta que no leíste en una carpeta que usas.

## Confirmado en la documentación oficial (consultada el 2026-10-26)

| Dato | Fuente |
| --- | --- |
| **Importaciones:** `@ruta/al/archivo` en `CLAUDE.md`; rutas relativas o absolutas, las relativas se resuelven desde el archivo que importa; **máximo cuatro saltos** de importación recursiva. No se expande dentro de fragmentos de código ni bloques; los espacios se escapan con barra invertida; una ruta entre comillas no se importa. Las importaciones de fuera del proyecto requieren aprobación por proyecto. | [How Claude remembers your project](https://code.claude.com/docs/en/memory) |
| **Modos de permisos:** `default` (Manual), `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`. `default` lee sin pedir; `acceptEdits` permite además ediciones y comandos comunes de archivos; `auto` revisa en segundo plano; `dontAsk` deniega lo que de otro modo pediría; `bypassPermissions` omite los controles de permisos y es solo para entornos aislados. **Un modo no es un sandbox ni una lista de control de acceso**, y `plan` no garantiza cero efectos. | [Choose a permission mode](https://code.claude.com/docs/en/permission-modes) |

No documentado en las fuentes consultadas: un límite de tamaño para `CLAUDE.md`; no lo supongas ni lo traslades a Claude Projects.

Lista completa de fuentes y salvedades: [`evidencia/plataformas-verificadas.md`](../../../evidencia/plataformas-verificadas.md).
