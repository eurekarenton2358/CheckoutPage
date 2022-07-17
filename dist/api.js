



const button = document.getElementById("paypal");

button.addEventListener('click', async () => {
  try {     
    const response = fetch("https://api.sandbox.checkout.com/payments", {
      method: "post",
headers:{"Authorization": "sk_test_0b9b5db6-f223-49d0-b68f-f6643dd4f808",
          "Content-Type":"application/json"},
    body: 
    {"source": {
        "type": "sofort"
              },
      "amount": 44600,
       "currency": "EUR",
    "reference": "request-05"
},
    });
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});