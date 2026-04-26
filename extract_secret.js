Java.perform(function () {

    function triggerPasswordBuild() {
        console.log("[*] Recherche d'une instance de MainActivity en cours...");

        Java.choose("com.pwnsec.firestorm.MainActivity", {
            onMatch: function (activityInstance) {
                console.log("[+] Instance trouvée : " + activityInstance);

                try {
                    var recoveredPassword = activityInstance.Password();
                    console.log("[+] Mot de passe récupéré : " + recoveredPassword);
                } catch (err) {
                    console.log("[-] Erreur pendant l'appel de Password() : " + err);
                }
            },

            onComplete: function () {
                console.log("[*] Fin de la recherche des instances.");
            }
        });
    }

    console.log("[*] Script chargé, attente avant exécution...");
    setTimeout(triggerPasswordBuild, 3500);
});