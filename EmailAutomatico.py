import smtplib
import email.message


def enviar_email(eemail):  
    corpo_email = f"""
    <p>bom dia, para redefinir sua senha, basta clicar no link e redefinir:</p>
    <p>http://127.0.0.1:5000/busca_email</p>
    <p>obs: sem aspas, sem colchetes e sem parenteses</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Recuperação de Senha"
    msg['From'] = 'luigiskyline4@gmail.com'
    msg['To'] = f'{eemail}'
    password = 'rzdrwbvgjgbudmko' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    return 'email enviado com sucesso'