# Roteiro do vídeo - AgroSat

Olá, somos o grupo responsável pelo projeto AgroSat.

O problema que escolhemos está relacionado ao agronegócio brasileiro. Muitas lavouras sofrem perdas porque pragas, doenças ou sinais de estresse são identificados tarde demais. Isso acontece porque o produtor muitas vezes depende de rondas manuais e não tem uma visão rápida da situação da plantação.

Nossa proposta é utilizar Visão Computacional para analisar imagens da lavoura em tempo real. O sistema captura vídeo pela webcam ou por um arquivo de vídeo, identifica regiões verdes associadas à vegetação e procura manchas amareladas ou marrons, que podem indicar pragas, doenças ou estresse na planta.

Agora vamos demonstrar o sistema funcionando.

Ao executar o projeto, a câmera é aberta e o OpenCV começa a processar os frames em tempo real. Na parte superior da tela, o sistema mostra o status da lavoura, o nível de risco, o percentual estimado de área afetada e uma recomendação para o produtor.

Quando o sistema identifica uma região suspeita, ele marca a anomalia com uma caixa na imagem. Se a área afetada for pequena, o risco é baixo. Se a quantidade de manchas aumentar, o sistema muda para alerta médio ou alto e recomenda uma inspeção na lavoura.

Essa solução pode ser aplicada no contexto da Global Solution porque ajuda o produtor rural a agir antes que o problema gere grandes prejuízos. Futuramente, o mesmo conceito pode ser integrado com drones, satélites, sensores IoT e dashboards agrícolas.

Obrigado.
