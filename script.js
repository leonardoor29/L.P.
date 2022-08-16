$( '#inputComit' ).click(
    function( ){
            // cadastro = 
            // {
            //    'nome' : document.getElementById('inputNome') .value,
            //    'Endereco' : document.getElementById('inputEndereco') .value,
            //    'email' : document.getElementById('inputEmail') .value
            // }   

            // alert('Meu nome é: ' + cadastro.nome + ' Sou de ' + cadastro.Endereco + 'Meu E-mail é: ' + cadastro.email);
            calculo = {
            'a' : document.getElementById('inputN1').value,
            'b' : document.getElementById('inputN2').value,
            'c' : document.getElementById('inputN2').value,
            }

            let media = (parseInt (calculo.a) + parseInt  (calculo.b) + parseInt (calculo.c)) / 3;

                if (media >= 7) {
                    alert("Você foi aprovado!");
                } else {
                    alert("Você foi reprovado");
                }
            // alert( 
                
            //     (parseInt (calculo.a) + parseInt  (calculo.b) + parseInt (calculo.c)) / 3);
            }
            
            )
            