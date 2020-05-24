using System.Collections;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using UnityEngine;

public class Cucaracha : MonoBehaviour
{

    public bool viva = true;

    
    void Update()
    {
        transform.position = new Vector3(-65.1f, 2.1f, -28.6f);
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "Cuerpo" && viva)
        {
            transform.rotation = Quaternion.EulerAngles(90f, 0, 0);
            viva = false;
        }
    }
}
