# Django ile Mikroservis Mimarisi

Bu proje, Django kullanarak mikro hizmet mimarisini keşfetmek ve uygulamak için tasarlanmıştır. Hizmet iletişimi, ölçeklenebilirlik ve hata toleransı gibi temel kavramlara odaklanarak, monolitik bir uygulamanın daha küçük, bağımsız olarak dağıtılabilir hizmetlere nasıl ayrılacağını gösterir.

## Bu Depoda Şunları Bulacaksınız:

- **Bireysel sorumlulukları olan birden fazla Django mikro hizmeti**: Her bir hizmet belirli bir işlevi yerine getirir ve bağımsız olarak ölçeklendirilebilir.
- **İstekleri uygun hizmetlere yönlendirmek için API Gateway**: API Gateway, mikro hizmetler arasındaki tüm istekleri yönlendirir ve merkezi bir erişim noktası sağlar.
- **REST veya mesaj aracıları (örn. RabbitMQ, Kafka) kullanarak servisler arası iletişim**: Servisler arası iletişim, REST API'leri veya mesaj aracılık sistemleri (RabbitMQ, Kafka gibi) kullanılarak sağlanır.
- **Her hizmet ve tüm sistem için Docker kullanarak konteynerleştirme**: Tüm mikro hizmetler Docker ile konteynerleştirilir, böylece her hizmet bağımsız olarak dağıtılabilir ve yönetilebilir.
- **Hizmet keşfi ve yük dengeleme stratejileri**: Hizmetler, dinamik olarak birbirlerini keşfeder ve yük dengeleme ile verimli bir şekilde çalışır.
- **Hizmetler arasında güvenli iletişim için uygulanan Kimlik Doğrulama ve Yetkilendirme**: JWT token tabanlı kimlik doğrulama ve yetkilendirme stratejileri, hizmetler arasında güvenli iletişimi sağlar.
- **JWT Token ile güvenli kimlik doğrulama**: Kullanıcıların kimlik doğrulaması, JSON Web Token (JWT) kullanılarak yapılır. Her hizmet, JWT token'ı doğrulayıp, kullanıcının kimliğini ve yetkilerini kontrol eder.
- **Veritabanı entegrasyonu**: Her mikro hizmetin kendi veritabanı vardır. PostgreSQL veya başka bir veritabanı kullanılarak her hizmetin veri yönetimi sağlanır. Ayrıca, mikro hizmetler arasında veri paylaşımı, uygun API çağrıları veya mesajlaşma sistemleri aracılığıyla yapılır.

## Kullanılan Teknolojiler

- Django
- Docker
- JWT (JSON Web Token)
- PostgreSQL (veya başka bir veritabanı)
- RabbitMQ / Kafka (isteğe bağlı)
- API Gateway
- Mikro hizmetler arası iletişim (REST API)

## Hedef

Bu proje, Django ile dağıtılmış sistemler oluşturmak ve mikro hizmetlerin ilkelerini anlamak isteyenler için bir öğrenme aracı olarak hizmet vermektedir. Ayrıca, JWT tabanlı güvenlik ve veritabanı entegrasyonu ile mikro hizmetler arasında güvenli ve verimli veri paylaşımını anlayacaksınız.

