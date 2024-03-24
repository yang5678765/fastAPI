**Create Account**
----
  Returns json data about the state of account creation.
* **URL**

    `/create_acount`
* **Method**

    `POST`
* **Data Params**

    `username`

    `password`
* **Succes Response**

    * **Code:** 201

      **Content:** {"success": true, "reason": ""}
* **Error Response**
    * **Code:** 400 Bad Request

      **Content:** {"success": false, "reason": "Username is too short."}
    * **Code:** 400 Bad Request

      **Content:** {"success": false, "reason": "Username is too long."}
    * **Code:** 400 Bad Request

      **Content:** {"success": false, "reason": "Password is too short."}
    * **Code:** 400 Bad Request

      **Content:** {"success": false, "reason": "Password is too long."}
    * **Code:** 400 Bad Request

      **Content:** {"success": false, "reason": "Passord should contain at least 1 uppercase letter, 1 lowercase letter, and 1 number."}
    * **Code:** 422 Unprocessable Entity

      **Content:** {"success": false, "reason":"Some error occurred during creating account."}
* **Sample Call**
    ```
    $.ajax({
        url: "/create_account",
        type : "POST",
        data: {
            "username":"testuser",
            "password":"Passw0rd"
        }
        success : function(r) {
        console.log(r);
        }
    });
    ```

**Verify Account and Password**
----
  Returns json data about account and password validation.
* **URL**

    `/verify_account`
* **Method**

    `POST`
* **Data Params**

    `username`

    `password`
* **Succes Response**

    * **Code:** 202

      **Content:** {"success": true, "reason": ""}
* **Error Response**
    * **Code:** 400 Bad Request

      **Content:** {"success": false, "reason": "Username is not exist."}
    * **Code:** 400 Bad Request

      **Content:** {"success": false, "reason": "Password is not correct."}
    * **Code:** 429 Too Many Requests

      **Content:** {"success": false, "reason": "Please wait for 1 minute to try again."}
    * **Code:** 400 Bad Request

      **Content:** {"success": false, "reason": "Some error occurred during verifying account."}

* **Sample Call**
    ```
    $.ajax({
        url: "/verify_account",
        type : "POST",
        data: {
            "username":"testuser",
            "password":"Passw0rd"
        }
        success : function(r) {
        console.log(r);
        }
    });
    ```

