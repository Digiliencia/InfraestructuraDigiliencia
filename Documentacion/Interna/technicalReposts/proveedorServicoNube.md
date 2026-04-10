# Informe comparativo de servicos VPS

Informe comparativo de ofertas de servicio  de VPS.

## Objetivos

El informe busca la mejor oferta para alojar el modelo de inteligencia artificial. Se compararán las ofertas de diferentes proveedores de VPS empresariales.

## Criterios de evaluación

Los criterios empleados para evaluar las alternativas son
- Precio
- Potencia gráfica (GPU)
- Características de la máquina
- Disponibilidad

## Ofertas

### Hostinger VPS

#### Servicios

- Procesadores AMD EPYC
- SSD NVMe
- Virtualización KVM
- Red: 1000Mbps simétricos
- Copias de seguridad y snapshots gratuitos
- Asistente IA
- Protección DDoS y firewall propio
- Servicio antivirus
- Fácilmente escalable

#### Precios

| Plan    | Precio mensual (24 meses) | vCPU | RAM   | Almacenamiento NVMe | Ancho de banda |
|---------|---------------------------|------|-------|---------------------|----------------|
| KVM 1   | 4,99 €          | 1    | 4 GB  | 50 GB               | 4 TB           |
| KVM 2   | 6,99 €                | 2    | 8 GB  | 100 GB              | 8 TB           |
| KVM 4   | 9,99 €                | 4    | 16 GB | 200 GB              | 16 TB          |
| KVM 8   | 19,99 €               | 8    | 32 GB | 400 GB              | 32 TB          |

| Plan    | Precio mensual (12 meses) | vCPU | RAM   | Almacenamiento NVMe | Ancho de banda |
|---------|---------------------------|------|-------|---------------------|----------------|
| KVM 1   | 5,99 €          | 1    | 4 GB  | 50 GB               | 4 TB           |
| KVM 2   | 8,49 €                | 2    | 8 GB  | 100 GB              | 8 TB           |
| KVM 4   | 12,99 €                | 4    | 16 GB | 200 GB              | 16 TB          |
| KVM 8   | 24,99 €               | 8    | 32 GB | 400 GB              | 32 TB          |

| Plan    | Precio mensual (1 mes) | vCPU | RAM   | Almacenamiento NVMe | Ancho de banda |
|---------|---------------------------|------|-------|---------------------|----------------|
| KVM 1   | 7,99 €          | 1    | 4 GB  | 50 GB               | 4 TB           |
| KVM 2   | 9,99 €                | 2    | 8 GB  | 100 GB              | 8 TB           |
| KVM 4   | 19,99 €                | 4    | 16 GB | 200 GB              | 16 TB          |
| KVM 8   | 38,99 €               | 8    | 32 GB | 400 GB              | 32 TB          |

#### Comentarios

No parece que existan planes personalizados con mayor capacidad. No cuentan con GPUs. Los VPS de Hostinger parecen enfocados a ofrecer infraestructura para servicios web, pero no computación en la nube.


### Oracle

Para valorar el uso de Oracle como proveedor de capacidad de cómputo se ha tenido en cuenta una única máquina virtual con capacidad gráfica. Oracle dispone de diferentes ofertas de máquinas con GPU dentro de las cuales se encuentran las siguientes:

| Modelo    | Unidades | Arquitectura | Ancho de banda  | Precio hora/GPU |
|---------|---------------------------|------|-------|---------------------|
| VM.GPU.A10.1 (new)   | 1x NVIDIA A10 Tensor Core          | Ampere    | 24 GB/sec  | 1.86€               |
| VM.GPU.A10.2 (new)   | 2x NVIDIA A10 Tensor Core          | Ampere    | 48 GB/sec  | 1.86€               |
| BM.GPU.A10.4 (new)   | 4x NVIDIA A10 Tensor Core          | Ampere    | 2x50 GB/sec  | 1.86€               |

Todas utilizan la arquitectura Ampere y las GPUs NVIDIA A10 la diferencia aparece en el número de GPUs disponibles así como en el ancho de banda disponible.

Los recursos de la máquina se muestran en la siguiente tabla.


| Shape    | OCPU | GPU Memory (GB) | CPU Memory (GB)  | Local DIsk (GB) | Max Network BandWidth |
|---------|---------------------------|------|-------|---------------------|----|
| VM.GPU.A10.2 (GPU: 2xA10)   | 30         | 48    | 4480  | 100| 48 Gbps                |

En conclusión, se estima un coste mensual total, suponiendo un uso diario de 3 horas, de 349.91€ al mes El desglose del precio es 345.96€ por la máquina y 3.95€ por el almacenamiento.

Para el resto de máquinas que pueden ser necesarias se podría utilizar o bien la máquina de acceso gratuito del mismo Oracle o al ser solo con intención de pruebas se pueden utilizar nuestros equipos.

La máquina de acceso gratuito de Oracle dispone de:
- 4 cores
- 24 GB RAM
- 200GB almacenamiento.
- Sin GPU.
  
#### Fuentes
- https://www.oracle.com/cloud/compute/gpu/pricing/
- https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.ht