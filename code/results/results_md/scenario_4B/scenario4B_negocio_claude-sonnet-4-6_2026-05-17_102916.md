# Gestión de Accesos Sospechosos con Cuentas Privilegiadas en Entidad Financiera

## Evaluación inicial de la situación

Antes de actuar, es importante entender que tienes **dos tensiones legítimas en conflicto**:
- Contener el incidente lo antes posible
- No interrumpir operaciones críticas del banco

Ambas son válidas, pero tienen **pesos diferentes**: la contención de un compromiso activo generalmente tiene prioridad sobre la operativa, aunque esto debe decidirse con información, no por defecto.

---

## Pasos inmediatos (primeras horas)

### 1. Activar el equipo de respuesta a incidentes
- Convocar a **Seguridad de la Información, IT, Riesgo Operacional y Cumplimiento** de forma simultánea
- Designar un responsable único de coordinación del incidente
- Abrir un canal de comunicación seguro y separado (no uses los sistemas potencialmente comprometidos)

### 2. Determinar si el acceso es activo o pasado
Esto cambia radicalmente la urgencia:
- ¿Las sesiones sospechosas siguen abiertas?
- ¿Hay actividad en curso en este momento?
- Si hay actividad activa, la contención es inmediata y no negociable

### 3. Preservar evidencias antes de cualquier acción
**Crítico y frecuentemente ignorado:**
- Capturar logs de sistemas, SIEM, Active Directory, VPN, accesos a aplicaciones
- No apagar sistemas comprometidos sin antes volcar memoria y logs
- Documentar con timestamps todo lo que se observe
- Esto es necesario tanto para el análisis forense como para el regulador

---

## Sobre el dilema de bloquear las cuentas

### Opciones intermedias que evitan el bloqueo total inmediato:

| Opción | Descripción | Cuándo usarla |
|--------|-------------|---------------|
| **Monitorización intensiva** | Vigilar en tiempo real sin bloquear | Si el acceso parece pasado y no hay actividad activa |
| **Rotación de credenciales** | Cambiar contraseñas y forzar re-autenticación | Casi siempre recomendable como primer paso |
| **Restricción de permisos temporal** | Reducir privilegios sin deshabilitar la cuenta | Si necesitas mantener operativa la cuenta |
| **Bloqueo con cuenta alternativa preparada** | Bloquear y tener lista una cuenta de emergencia auditada | Si hay actividad activa o riesgo alto |
| **Segmentación de red** | Aislar sistemas afectados sin tocar cuentas | Para contener movimiento lateral |

### Mi recomendación sobre el bloqueo:
Si no sabes si el acceso fue legítimo o no, **la rotación de credenciales es el mínimo aceptable de forma inmediata**. El bloqueo completo depende de si hay actividad activa y del nivel de riesgo que determine tu equipo de seguridad con los datos disponibles.

---

## Análisis forense: qué necesitas saber

Debes responder estas preguntas con evidencia, no con suposiciones:

- ¿Desde qué IPs/dispositivos se produjeron los accesos?
- ¿A qué sistemas específicos se accedió?
- ¿Se ejecutaron comandos, scripts o se modificaron configuraciones?
- ¿Se accedió a datos de clientes, transacciones o sistemas de pagos?
- ¿Hubo movimiento lateral hacia otros sistemas?
- ¿Se crearon nuevas cuentas o se modificaron permisos?
- ¿Hay indicios de exfiltración de datos (volúmenes de transferencia anómalos)?

---

## Obligaciones regulatorias (contexto financiero europeo/español)

Esto es especialmente relevante en banca:

### DORA (Digital Operational Resilience Act)
- Aplicable desde enero 2025
- Obliga a notificar incidentes TIC significativos al supervisor competente
- Tienes que evaluar si este incidente supera los umbrales de notificación

### RGPD / LOPDGDD
- Si se ha accedido a datos personales de clientes, **tienes 72 horas para notificar a la AEPD** desde que tienes conocimiento del incidente
- El reloj corre desde que tienes "conocimiento razonable", no desde que tienes certeza total

### Banco de España / BCE
- Dependiendo de tu tamaño y naturaleza, puede haber obligaciones adicionales de reporte
- Consulta con tu equipo legal y de cumplimiento de forma inmediata

### Recomendación práctica:
**Involucra a tu DPO y al equipo legal ahora**, no cuando tengas el análisis completo. Ellos necesitan tiempo para evaluar las obligaciones de notificación en paralelo.

---

## Comunicación interna

- **Limita el conocimiento** del incidente a quienes necesitan saberlo (need-to-know)
- Informa a la **Alta Dirección y al Consejo** si el riesgo es significativo
- No comuniques por canales que puedan estar comprometidos
- Documenta todas las decisiones tomadas y sus justificaciones

---

## Lo que no deberías hacer

- ❌ Apagar sistemas sin capturar evidencias primero
- ❌ Intentar "limpiar" el incidente antes de analizarlo
- ❌ Asumir que fue un acceso legítimo sin verificarlo
- ❌ Asumir que fue un ataque sin verificarlo tampoco
- ❌ Demorar la notificación regulatoria esperando tener toda la información
- ❌ Gestionar esto solo desde IT sin involucrar negocio, riesgo y legal

---

## Resumen de prioridades

```
1. Preservar evidencias
2. Determinar si el acceso es activo
3. Contener según el riesgo real (rotación de credenciales como mínimo)
4. Analizar el alcance
5. Cumplir obligaciones de notificación regulatoria
6. Remediar y reforzar controles
```

---

¿Tienes ya información sobre si los accesos son recientes o activos, o sobre qué sistemas específicos se vieron afectados? Con más contexto puedo ayudarte a priorizar mejor los pasos concretos.