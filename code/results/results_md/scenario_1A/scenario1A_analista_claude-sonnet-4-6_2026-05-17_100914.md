# Respuesta a Incidente de Ransomware en Plataforma de Pagos

Dado el contexto crítico (entidad financiera + plataforma de pagos + posible exfiltración de datos), aquí tienes una guía estructurada por prioridades:

---

## 🔴 FASE 1: Contención Inmediata (Primeras horas)

### Aislamiento
- **Segmentar inmediatamente** los sistemas afectados de la red
- Desconectar conexiones con terceros, proveedores y sistemas de pago externos (SWIFT, pasarelas, etc.)
- **No apagar** los sistemas afectados todavía → perderías evidencia en memoria RAM
- Bloquear cuentas de servicio y credenciales potencialmente comprometidas

### Preservación de evidencia
- Capturar **volcados de memoria RAM** de sistemas afectados antes de cualquier acción
- Preservar logs: firewall, SIEM, EDR, Active Directory, VPN, accesos a BBDD
- Documentar con timestamps todo lo que hagas desde este momento

### Comunicación interna urgente
- Activar el **Plan de Respuesta a Incidentes** si existe
- Escalar a CISO, CTO y Dirección inmediatamente
- Constituir el **equipo de crisis** (IT, Legal, Comunicación, Negocio)

---

## 🟠 FASE 2: Evaluación del Alcance (Primeras 24-48h)

### Análisis técnico
```
Preguntas clave a responder:
├── ¿Qué sistemas están cifrados vs. comprometidos vs. limpios?
├── ¿Cuál es el vector de entrada? (phishing, RDP expuesto, supply chain...)
├── ¿Hay indicios de exfiltración? (tráfico anómalo, herramientas de staging)
├── ¿Qué cuentas privilegiadas pueden estar comprometidas?
└── ¿Cuánto tiempo lleva el atacante dentro? (dwell time)
```

### Identificar el ransomware
- Usar herramientas como **ID Ransomware** (nomoreransom.org)
- Buscar IOCs en fuentes como VirusTotal, MISP, o feeds del sector financiero (FS-ISAC)
- Revisar si el grupo tiene historial de **doble extorsión** (cifrado + exfiltración)

### Revisar backups
- Verificar integridad y disponibilidad de backups
- Comprobar si los backups también están afectados (es habitual que el ransomware los ataque primero)
- Identificar el **último punto de restauración limpio**

---

## 🟡 FASE 3: Obligaciones Regulatorias (Plazos críticos)

> ⚠️ Como entidad financiera en España/UE tienes obligaciones legales con plazos muy estrictos

### DORA (si aplica desde enero 2025)
- Notificación de incidente mayor al **supervisor competente** (BCE/BdE/CNMV según tu caso)
- Informe inicial: **4 horas** desde clasificación como incidente mayor
- Informe intermedio y final con plazos adicionales

### RGPD / LOPDGDD
- Si hay **indicios de afectación de datos personales**: notificación a la **AEPD en 72 horas**
- Evaluar si requiere comunicación a los interesados (clientes afectados)

### Banco de España / CNMV
- Notificación según normativa de continuidad operacional
- Posible comunicación a sistemas de pago (SEPA, Banco de España)

### ENS (si aplica)
- Notificación al **CCN-CERT** si estás en el ámbito del ENS

---

## 🔵 FASE 4: Recursos Externos

### Contactar inmediatamente
| Recurso | Cuándo |
|---|---|
| **INCIBE-CERT** (017) | Soporte técnico, coordinación |
| **CCN-CERT** | Si hay sistemas bajo ENS o infraestructura crítica |
| **Policía Nacional / Guardia Civil** (GDT/BIT) | Para denuncia formal |
| **Empresa forense externa** | Si no tienes capacidad interna |
| **Aseguradora de ciberriesgo** | Activar póliza si existe |

### No contactar al atacante sin asesoramiento legal
- El pago del rescate **no garantiza** recuperación ni no publicación
- Puede tener implicaciones legales (sanciones OFAC si el grupo está sancionado)

---

## ⚫ Errores críticos a evitar

```
❌ Apagar sistemas sin capturar evidencia
❌ Intentar descifrar archivos sin análisis previo
❌ Comunicar públicamente sin coordinación legal/comunicación
❌ Reconectar sistemas sin verificar que están limpios
❌ Ignorar los plazos regulatorios
❌ Pagar el rescate como primera opción
❌ Usar los mismos canales de comunicación potencialmente comprometidos
```

---

## 📋 Checklist de las próximas horas

- [ ] Sistemas afectados aislados
- [ ] Evidencia preservada (RAM + logs)
- [ ] Equipo de crisis convocado
- [ ] Backups verificados
- [ ] Asesor legal notificado
- [ ] Reguladores notificados (según plazos)
- [ ] Canal de comunicación alternativo establecido (fuera de banda)
- [ ] Empresa forense/IR externa contratada si es necesario

---

¿En qué fase estás ahora mismo o qué aspecto necesitas profundizar? Puedo ayudarte con el análisis técnico, la redacción de notificaciones regulatorias, o la estrategia de recuperación.