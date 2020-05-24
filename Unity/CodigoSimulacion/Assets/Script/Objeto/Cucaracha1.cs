using System.Collections;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using UnityEngine;

public class Cucaracha1 : MonoBehaviour
{

    public bool viva = true;

    void Update()
    {
        transform.position = new Vector3(-19f, 2.1f, -55.5f);
        
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
