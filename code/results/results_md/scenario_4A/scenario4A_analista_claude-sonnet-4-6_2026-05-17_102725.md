# Respuesta a Incidente de Seguridad - Accesos Sospechosos con Cuentas Privilegiadas

Este es un escenario de alta criticidad. Te estructuro una respuesta ordenada por fases:

---

## 🔴 FASE 1: Contención Inmediata (primeras horas)

**Acciones prioritarias:**
- **Deshabilitar o aislar** las cuentas comprometidas sospechosas *sin eliminarlas* (preservar evidencia)
- **Revocar sesiones activas** de esas cuentas en todos los sistemas
- **Bloquear las IPs** de origen sospechoso en firewall/WAF
- Notificar al **CISO y equipo de respuesta a incidentes** formalmente
- **Activar el plan de respuesta a incidentes** si tu organización lo tiene documentado

> ⚠️ **Importante:** No apagues sistemas comprometidos todavía. Perderías evidencia volátil (memoria RAM, conexiones activas).

---

## 🟡 FASE 2: Identificación y Análisis Forense

### Recopilación de evidencia (con cadena de custodia)
```
- Logs de autenticación (SIEM, Active Directory, LDAP)
- Logs de acceso a sistemas internos y bases de datos
- Registros de VPN y accesos remotos
- Capturas de tráfico de red si están disponibles
- Logs de cambios de configuración (change management)
```

### Preguntas clave a responder
- ¿Cuándo comenzó la actividad anómala exactamente?
- ¿Qué sistemas tocaron esas cuentas?
- ¿Se crearon nuevas cuentas o se modificaron permisos?
- ¿Hubo exfiltración de datos? (volumen de tráfico saliente inusual)
- ¿Las credenciales fueron robadas o son cuentas internas?

### Herramientas útiles
- Análisis de logs con **Splunk, ELK, Microsoft Sentinel**
- Revisión de **Event IDs críticos en Windows:** 4624, 4625, 4648, 4672, 4720, 4732
- Verificar integridad de configuraciones con herramientas de **baseline comparison**

---

## 🟠 FASE 3: Evaluación del Alcance

**Determinar si hubo:**

| Área | Qué verificar |
|------|--------------|
| Configuraciones | Cambios en ACLs, GPOs, reglas de firewall, usuarios admin |
| Datos sensibles | Acceso a BBDDs con datos de clientes, transacciones |
| Persistencia | Nuevas cuentas, backdoors, tareas programadas |
| Movimiento lateral | Accesos a otros sistemas desde el punto inicial |

---

## 🔵 FASE 4: Obligaciones Regulatorias (crítico en banca)

Como entidad financiera tienes **plazos legales estrictos:**

- **DORA (si operas en UE):** Notificación de incidentes mayores en plazos definidos
- **GDPR/LOPD:** Si hay datos personales afectados, notificación a la **AEPD en 72 horas**
- **Banco de España / BCE:** Según criticidad del incidente
- **Comunicación interna:** Dirección, Compliance, Asesoría Jurídica

> 📋 Documenta **todo** desde el primer momento con timestamps precisos

---

## 🟢 FASE 5: Erradicación y Recuperación

- Cambio de credenciales de **todas** las cuentas privilegiadas
- Revisión y hardening de configuraciones afectadas
- Implementar **MFA** si no estaba activo en esas cuentas
- Restaurar desde backups verificados si hay sistemas comprometidos
- Monitorización intensiva post-incidente

---

## 📋 Recomendaciones Adicionales

**A corto plazo:**
- Auditoría completa de cuentas con privilegios elevados
- Revisar política de acceso desde ubicaciones externas
- Implementar alertas de comportamiento anómalo (UEBA)

**Estructurales:**
- Principio de **mínimo privilegio** en cuentas de servicio
- **PAM (Privileged Access Management)** si no lo tenéis
- Segmentación de red para limitar movimiento lateral

---

## ⚡ Resumen de Prioridades Inmediatas

```
1. Contener sin destruir evidencia
2. Activar equipo de respuesta formal
3. Preservar logs con cadena de custodia
4. Evaluar obligación de notificación regulatoria
5. Determinar alcance real antes de comunicar externamente
```

---

¿Quieres que profundice en alguna fase específica, en los requisitos regulatorios concretos o en las herramientas de análisis forense?