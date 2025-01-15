# It is necessary to install ChromaDB(pip install chromadb) and Ollama(pip install chromadb)
# Also, you should run Llama 3.2 via Ollama on your machine before running this script
import chromadb
from ollama import chat
from ollama import ChatResponse

client = chromadb.Client()

collection = client.create_collection("faq-document")
collection.add(
    documents=[
    'Como emitir notas fiscais no aplicativo Aegro Negócios? : Agora você pode emitir a nota fiscal eletrônica direto do celular com o aplicativo Aegro Negócios. Confira o que é necessário para começar a emitir: Primeiro, certifique-se que você está habilitado para emitir NFe, esse credenciamento é feito pela sefaz do seu estado. Depois, veja se já possui certificado digital, caso não, temos uma parceria com a Rede Ideia para adquirir seu certificado digital, clique para saber mais. Mas não se preocupe, você consegue testar o Aegro sem certificado também, precisará dele apenas para finalizar o processo. Ao abrir para uma nova emissão encontrará campos a serem preenchidos, dos quais estarão com a margem cinza, isso significa que ainda está pendente: Assim, iremos seguir cada espaço: Emitente: Aqui será preenchido com as informações do emitente que deseja que seja o responsável pelas emissões de notas. Além de dados básicos como nome e endereço, também será o espaço que você adicionará a inscrição estadual, série e número, certificado e opção do FUNRURAL (caso tenha dúvida no FUNRURAL, contate o seu contador). Pode ser cadastrado mais de um emitente, mesmo que este esteja com o mesmo CPF, ou seja, cada inscrição estadual pode ter o seu cadastro próprio, do qual pode ser adicionado por esse caminho, ou acessando o ícone de emitente, a partir da tela inicial, no canto direito da tela. Este ícone também englobará os fornecedores. Ao terminar o preenchimento todos os ícones laterais deverão estar verdes, caso tenha algo ainda a ser feito, ele será apresentado com a lateral vermelha. Ainda, o progresso do preenchimento também será indicado no ícone da lateral direita, no canto de baixo da tela, ao expandir, estará demonstrando o que tem pendente. Havendo tudo finalizado estará no momento de conferir a DANFE, clicando em conferir detalhes: Neste momento você terá o documento auxiliar da nota fiscal para conferir, antes da emissão, podendo salvar o PDF e compartilhar para conferência antes do envio a SEFAZ. Cabe ressaltar que ainda não é a emissão efetivamente, então alguns campos ainda não serão os finais, como a série e número, que sempre aparecerão como 1, mas na nota estarão de acordo com o seu cadastro no emitente. Emiti, e agora? Quando você clica em confirmar emissão, ela será enviada para a Sefaz, e caso esteja tudo certo, voltará com status autorizada. A sua nota poderá ainda ser rejeitada pela Sefaz, mas calma, a rejeição virá com uma descrição do que você precisa resolver, em tendo o ajuste feito, é só enviar novamente. Todas as notas estarão disponíveis na tela de listagem!',
    'Quem pode usar o Aegro Negócios ? : O Aegro Negócios é uma aplicação gratuita que pode ser utilizada por todos, que já está disponível para Android e em breve para IOS.',
    'Preciso ter uma conta no Aegro para usar o Aegro Negócios? : Não precisa ter uma conta para usar o Aegro Negócios. Contudo, se utilizar uma conta sua experiência será mais rica, pois mais funcionalidades e configurações estarão disponíveis.',
    'O que é uma versão prévia ? : Uma versão prévia é uma versão que está disponível para ser utilizada pelo público, mas que ainda não conta com todas as funcionalidades que foram pensadas. Ao longo do tempo novas funcionalidades serão adicionadas e/ou funcionalidades existentes modificadas até que todas as funcionalidades pensadas pela Aegro tenham sido publicadas. Você pode nos ajudar a estabelecer as funcionalidades utilizando as funcionalidades de envio de sugestões e comentários.',
    'Que serviços o Aegro Negócios me oferece ? : O Aegro Negócios oferecerá diversos serviços. Entre eles, notícias sobre o mundo do Agro Negócio e de cotações de commodities agrícolas e não agrícolas. Estão planejadas outras funcionalidades como informações climáticas e um calculador e comparador de produtividade, entre outros.'
],
    ids=['doc1', 'doc2', 'doc3', 'doc4', 'doc5'],
)

while True:

    question = input("\n\nFaça uma pergunta sobre o app Aegro Negócios ou digite \"sair\" para terminar o programa")
    if question == "sair":
        break

    results = collection.query(
        query_texts=[question],
        n_results=1,
    )

    similar_text_to_enrich_prompt = results['documents'][0][0]

    response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': f"""
            {question}\n\n
            Use somente as informações relevantes do texto abaixo para ajudar na resposta:
            {similar_text_to_enrich_prompt}
    """,
        },
    ])

    print(response.message.content)
