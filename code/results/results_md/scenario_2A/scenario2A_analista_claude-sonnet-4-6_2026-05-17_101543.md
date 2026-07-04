# Respuesta a Incidente: Repositorio Expuesto con Datos de Clientes

## Acción Inmediata (Primeros 30 minutos)

### 1. Contención
- **Corregir la mala configuración** y cerrar el acceso público inmediatamente si no se ha hecho ya
- **Revocar credenciales** de acceso al repositorio como medida preventiva
- **Preservar el estado actual** antes de hacer cambios: captura de logs, configuración actual, snapshots
- **No borrar ni modificar evidencias** — esto es crítico para la investigación y para el regulador

### 2. Activar el equipo de respuesta
- Escalar a CISO / responsable de seguridad
- Notificar al equipo legal y de cumplimiento normativo
- Activar el protocolo de gestión de incidentes si existe

---

## Investigación Forense (Primeras horas)

### Qué necesitas determinar con urgencia:

| Pregunta | Fuente de datos |
|---|---|
| ¿Qué IPs accedieron y cuándo? | Logs del servidor / WAF / CDN |
| ¿Qué métodos HTTP se usaron? (GET, HEAD...) | Access logs |
| ¿Qué volumen de datos se transfirió? | Bytes transferidos en logs |
| ¿Qué archivos o rutas fueron solicitados? | Request logs |
| ¿Hubo autenticación o acceso anónimo? | Auth logs |
| ¿Las IPs están asociadas a actores conocidos? | Threat intelligence |

### Análisis de logs:
```
# Ejemplo de lo que buscar en access logs
- Respuestas 200 con bytes_sent > 0 → descarga confirmada
- Respuestas 206 → descarga parcial (también relevante)
- Patrones de scraping: muchas peticiones en poco tiempo
- User-agents inusuales o automatizados
```

---

## Obligaciones Regulatorias — **Plazos críticos**

### RGPD / LOPDGDD (si hay datos de personas físicas):
> ⚠️ **72 horas desde que tienes conocimiento del incidente** para notificar a la AEPD si existe riesgo para los derechos y libertades de los afectados

- La notificación debe hacerse aunque **no tengas toda la información** — se puede complementar después
- Evalúa si el riesgo es **alto** → puede requerir también notificar a los **clientes afectados**
- Documenta la decisión aunque decidas que no es notificable

### Banco de España / CNMV / regulador sectorial:
- Revisa tus obligaciones específicas como entidad financiera (DORA si aplica, Circular BdE, etc.)
- Muchos reguladores financieros tienen sus propios plazos de notificación de incidentes

### Recomendación práctica:
**Involucra a legal desde el minuto uno** — la decisión de notificar o no al regulador no debe tomarla solo el equipo técnico.

---

## Evaluación del Riesgo

### Factores que determinan la gravedad:
- **Tipo de datos expuestos**: ¿datos de identificación, financieros, contraseñas, datos especialmente protegidos?
- **Volumen**: número de clientes potencialmente afectados
- **Evidencia de exfiltración**: bytes transferidos en logs
- **Sensibilidad del repositorio**: ¿había credenciales, tokens, datos en claro?

### Escenarios posibles:
```
Sin descarga confirmada + IPs de bots/crawlers genéricos
→ Riesgo menor, pero documenta y evalúa notificación

Con descargas confirmadas + IPs desconocidas
→ Brecha de datos confirmada, notificación AEPD muy probablemente obligatoria

Datos sensibles + descarga masiva
→ Notificación a afectados probablemente requerida
```

---

## Documentación del Incidente

Desde ahora mismo, registra todo:
- **Timeline** detallado de eventos (cuándo ocurrió, cuándo se detectó, cada acción tomada)
- **Decisiones tomadas y por quién**
- **Evidencias recopiladas** con cadena de custodia
- **Comunicaciones internas**

> Esto es esencial tanto para el regulador como para una posible investigación posterior.

---

## Lecciones Aprendidas (Post-incidente)

Una vez contenido el incidente:
- Revisión de **todos los repositorios** con configuración similar
- Implementar **monitorización de accesos** y alertas sobre datos sensibles
- Revisar el proceso de **gestión de configuraciones** (¿cómo llegó a estar expuesto?)
- Formación si hubo error humano

---

## Resumen de Prioridades

```
1. CONTENER → cerrar acceso y preservar evidencias
2. INVESTIGAR → determinar si hubo exfiltración real
3. NOTIFICAR → AEPD en <72h si aplica (no esperes a tener certeza total)
4. DOCUMENTAR → todo, desde el primer momento
5. REMEDIAR → corregir causa raíz y revisar sistemas similares
```

---

¿Quieres que profundice en algún aspecto concreto, como el análisis de logs, la redacción de la notificación a la AEPD, o la comunicación a clientes afectados?