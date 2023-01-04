# pdf-e-email-autom-tico
Neste projeto, incrementei a um primeiro projeto cujo objetivo é gerar automaticamente pdf's contendo orçamentos de serviço de Social Media, a função de envio automático de email, com mensagem contendo dados personalizados e anexo do pdf gerado.

Na primeira etapa do código, acolho em váriaveis, as informações relevantes do orçamento.
Através da biblioteca FPDF, o programa utiliza template previamente montado, para alocar as informações das variáveis, criando automáticamente arquivo PDF devidamente estruturado para enviar ao cliente.

Na segunda fase do projeto, utiliza-se as bibliotecas pyautogui e pyperclip, para comandos de  memória de texto e comandos de mouse.
Através das bibliotecas, atribui-se automaticamente os comandos de abertura de nova aba, digitar o endereço de site do Gmail, clicar em novo email, atribuir destinatário e assunto. No corpo do texto o programa cria uma váriavel de mensagem, com texto padrão, exceto nas informações de orçamentos que são alocadas de acordo com as varáveis respectivas da primeira fase do código.
Por fim, através de auto clique, o programa atribui o anexo do pdf e envia o email ao destinatário.
