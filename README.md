# giga-factory-access-control
Projet-Contrôle d'accès Giga Factory (BTS)

Ce projet implémente un système de cotrôle d'accès pour une Giga Factory structuré en trois packages principaux :

-**Authentification centralisée** : API Flask connectée à un annuaire LDAP (OpenLdap)
-**Application embarquée** : interface côté borne /terminal d'accès
-**Supervision** : suivi et journalisation des tentatives d'accès

---

## 1. Architecture globale

- **LDAP/OpenLDAP** : stocke les utilisateurs et leurs informations (uid, mot de passe, etc)
- **Backend Flask** : consomme l'API Flask pour valider les accès
- **Supervision** : centralise les logs d'authentification

---

## 2. Package Authentification centralisée

Permettre à une application cliente d'envoyer des données (badge) qui seront envoyées à l'annuaire et vérifiées

## 3. Package Application embarquée

## 4. Supervision 
