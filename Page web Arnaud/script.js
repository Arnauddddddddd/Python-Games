function Fonction1()

{
if (document.getElementById('oui').checked)
     
     {
     alert("Super ! Vous pouvez continuer")
       }
       
if (document.getElementById('non').checked)
     
     {
     alert('Revenez plus tard, ici on veut une bonne note')
       }

}




function MotDePasse()

{
 MDP = document.getElementById("zoneMDP").value;
if (MDP == "FACE66270") 
   {
     window.location=("page5.html");
    }
 
else
    {
    alert("Désolé mais ce n'est pas le bon mot de passe");
     }
 
 }
 

function video()
{

window.open('https://www.youtube.com/watch?v=Ad9uswL727w&ab_channel=St%C3%A9phaneBonnaud', target="_blank") ;

}