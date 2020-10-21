#Passing Functions as Parameters

#kodingan js
# function formalGreeting() {
#   console.log("How are you?");
# }function casualGreeting() {
#   console.log("What's up?");
# }function greet(type, greetFormal, greetCasual) {
#   if(type === 'formal') {
#     greetFormal();
#   } else if(type === 'casual') {
#     greetCasual();
#   }
# }// prints 'What's up?'
# greet('casual', formalGreeting, casualGreeting);


#kodingan python
def formalGreeting(selamat, siang, semua):
	print(f'formalGreeting {selamat}') 	
	print(f'formalGreeting {selamat} {siang}') 	
	print(f'formalGreeting {selamat} {siang} {semua}') 		

formalGreeting('selamat', 'siang', 'semua')