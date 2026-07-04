# Gestión de Vulnerabilidad Crítica de Proveedor Externo

## Evaluación inicial de la situación

Antes de actuar, conviene clarificar lo que sabes y lo que no sabes:

| Conocido | Desconocido |
|----------|-------------|
| Vulnerabilidad crítica confirmada por proveedor | Naturaleza técnica exacta del fallo |
| Sin indicios de explotación (por ahora) | Impacto real sobre tus sistemas |
| Proveedor aplicando mitigación | Plazo de resolución definitiva |
| Afecta a banca online | Si hay otros proveedores afectados |

---

## Acciones inmediatas (primeras horas)

### 1. Activar el proceso interno
- **Notifica a tu responsable** y al equipo de gestión de incidentes aunque no haya explotación confirmada → una vulnerabilidad crítica en banca online justifica activación preventiva
- **Revisa tu política de gestión de vulnerabilidades y terceros**: puede haber obligaciones de escalado con plazos definidos
- **Abre un ticket/registro formal** desde el primer momento para trazabilidad

### 2. Obtener información técnica del proveedor
Solicita formalmente y por escrito:
- CVE o identificador interno de la vulnerabilidad
- Sistemas y versiones afectadas
- Naturaleza del riesgo (RCE, fuga de datos, bypass de autenticación...)
- Detalles de la mitigación aplicada y su efectividad
- Fecha estimada de parche definitivo
- Si han notificado a otros clientes y si hay explotación conocida en el sector
- Confirmación de si han realizado análisis forense en sus sistemas

> ⚠️ **No aceptes solo comunicación verbal**: necesitas documentación escrita para cumplimiento regulatorio

---

## Análisis de impacto propio

### Mapeo técnico
- ¿Qué componentes concretos del proveedor usas y en qué arquitectura?
- ¿Tienes acceso directo a esos sistemas o están completamente en su infraestructura?
- ¿Qué datos fluyen por esos sistemas? (credenciales, datos de pago, datos personales...)
- ¿Existen controles compensatorios ya activos? (WAF, segmentación, monitorización)

### Revisión de logs y monitorización
- Aunque no haya indicios, **revisa logs retroactivamente** buscando anomalías relacionadas con los sistemas afectados
- Aumenta el nivel de alerta/monitorización sobre esos componentes
- Define indicadores de compromiso (IoCs) si el proveedor puede facilitarlos

---

## Obligaciones regulatorias — Aspecto crítico

En el sector financiero español/europeo debes considerar:

### DORA (Reglamento UE 2022/2554)
- Aplica desde enero 2025
- Exige gestión de riesgos de terceros TIC y notificación de incidentes graves
- Evalúa si esto constituye un **incidente significativo** según tus criterios internos

### Banco de España / BCE / CNMV
- Revisa si existe obligación de notificación preventiva según tu categoría de entidad

### RGPD / LOPDGDD
- Si hay riesgo de exposición de datos personales, el plazo de notificación a la AEPD es **72 horas** desde que se tiene conocimiento del incidente
- Aunque no haya explotación confirmada, valora si el riesgo potencial obliga a notificación

### NIS2
- Si tu entidad está en el ámbito de aplicación, revisa obligaciones de notificación

> 💡 **Recomendación**: Involucra a tu DPO y asesoría jurídica desde el principio, no al final

---

## Gestión del proveedor

### Contractual
- Revisa el contrato: ¿qué SLAs de seguridad existen? ¿hay obligaciones de notificación del proveedor?
- ¿Tienes derecho de auditoría o a solicitar un informe de terceros (pentest, certificación)?

### Medidas de presión/control
- Solicita un **informe de remediación** con plazos concretos
- Valora si la mitigación aplicada es suficiente o si debes exigir medidas adicionales
- Considera si es necesario **suspender temporalmente** alguna funcionalidad mientras se resuelve (análisis coste/beneficio)

---

## Comunicación interna

```
Nivel de escalado sugerido:
├── CISO / Director de Seguridad → inmediato
├── CTO / Responsable de Sistemas → inmediato  
├── DPO → en paralelo
├── Área jurídica/Compliance → en paralelo
├── Dirección general → según criticidad y política interna
└── Comité de crisis → si se confirma explotación o impacto real
```

---

## Lo que NO debes hacer

- ❌ Esperar pasivamente a que el proveedor resuelva sin seguimiento activo
- ❌ Asumir que "sin explotación conocida = sin urgencia"
- ❌ Gestionar esto solo sin escalar internamente
- ❌ Dejar pasar el plazo de 72h del RGPD si hay riesgo real para datos personales
- ❌ Comunicar públicamente o a clientes sin coordinación con dirección y legal

---

## Resumen de prioridades

```
AHORA (horas)     → Escalar internamente + solicitar info técnica al proveedor
CORTO PLAZO       → Análisis de impacto propio + revisión de logs
PARALELO          → Evaluar obligaciones regulatorias con DPO y legal
SEGUIMIENTO       → Control del plan de remediación del proveedor
CIERRE            → Lecciones aprendidas + revisión del proceso de terceros
```

---

¿Quieres que profundice en algún aspecto concreto, como los criterios de notificación regulatoria, cómo estructurar la comunicación con el proveedor, o el análisis técnico de impacto?