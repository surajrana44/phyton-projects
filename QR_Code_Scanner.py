
""" 
QR Code Scanner using Python

## step to build qr code scanner using python
1. Install the required libraries:
2.taking input from user for their upi id
3. payment url 
4.qr code generation
5.qr code download
6. qr code scanning

"""

import qrcode

upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#defining the payment URL based on the UPI ID and payment app
 
phonepe_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
goople_pay_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#crate a QR code for each payment app

phonepe_url= qrcode.make(phonepe_url)
paytm_url = qrcode.make(paytm_url)
goople_pay_url = qrcode.make(goople_pay_url)

#save the QR code images
phonepe_url.save('phonepe_qr.png')
paytm_url.save('paytm_qr.png')
goople_pay_url.save('google_pay_qr.png')

# Display the QR codes 
phonepe_url.show()
paytm_url.show()
goople_pay_url.show()