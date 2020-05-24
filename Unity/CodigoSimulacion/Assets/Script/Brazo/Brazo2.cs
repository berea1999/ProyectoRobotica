using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Runtime.CompilerServices;
using UnityEditor;
using UnityEngine;

public class Brazo2 : MonoBehaviour
{
    public float rotacion = 50;
    public float movimiento = 30;

    float xRotation;
    float yRotation;
    float zRotation;

    Vector3 Pos;
    public GameObject Cuerpo;

    bool klk = true;
    bool wON = true;
    bool sON = false;
   
    // Start is called before the first frame update
    void Start()
    {
        transform.position = new Vector3(9.8f, 5.8f, -80.39f);

        xRotation = transform.localEulerAngles.x;
        yRotation = transform.localEulerAngles.y;
        zRotation = transform.localEulerAngles.z;
    }

    // Update is called once per frame
    void Update()
    {
        Movimiento();
        Rotacion();
        ComprobacionSubirBajar();
    }


    void Movimiento()
    {
        if (Input.GetKey(KeyCode.UpArrow) && wON)
        {
            transform.Translate(Vector3.forward * movimiento * Time.deltaTime); //mover adelante
        }

        if (Input.GetKey(KeyCode.DownArrow) && wON)
            transform.Translate(Vector3.back * movimiento * Time.deltaTime); //mover atras
    }


    void Rotacion()
    {
        if (Input.GetKey(KeyCode.RightArrow))
        {
            transform.RotateAround(Cuerpo.transform.position, Vector3.up, rotacion * Time.deltaTime);
        }

        if (Input.GetKey(KeyCode.LeftArrow))
        {
            transform.RotateAround(Cuerpo.transform.position, Vector3.up, -rotacion * Time.deltaTime);
        }

        //Movimiento hacia ATRÁS la rotación se invierte
        if (Input.GetKey(KeyCode.RightArrow) && Input.GetKey(KeyCode.DownArrow) && !Input.GetKey(KeyCode.UpArrow))
        {
            transform.RotateAround(Cuerpo.transform.position, Vector3.up, -rotacion * 2 * Time.deltaTime);
        }

        if (Input.GetKey(KeyCode.LeftArrow) && Input.GetKey(KeyCode.DownArrow) && !Input.GetKey(KeyCode.UpArrow))
        {
            transform.RotateAround(Cuerpo.transform.position, Vector3.up, rotacion * 2 * Time.deltaTime);
        }

        //Actualizamos rotaciones
        yRotation = transform.localEulerAngles.y;
        zRotation = transform.localEulerAngles.z;
    }

    void ComprobacionSubirBajar() //Levanta o baja brazo
    {
        if (!Input.GetKey(KeyCode.UpArrow) && !Input.GetKey(KeyCode.DownArrow))
        {

            if (Input.GetKey("w") && klk && wON) //Levanta brazo
            {
                StartCoroutine("waitXup");
            }


            if (Input.GetKey("s")&& klk && sON) //Baja brazo
            {
                StartCoroutine("waitXdown");
            }
            xRotation = transform.localEulerAngles.x;

        }        
    }
    IEnumerator waitXup()
    {
        klk = false;
        wON = false;
        for (int i = 0; i < 130; i++)
        {
            yield return new WaitForSecondsRealtime(0.03f);
            transform.Rotate(-1, 0, 0);
        }
        klk = true;
        sON = true;
    }

    IEnumerator waitXdown()
    {
        klk = false;
        sON = false;
        for (int i = 0; i < 130; i++)
        {
            yield return new WaitForSecondsRealtime(0.03f);
            transform.Rotate(1, 0, 0);
        }
        klk = true;
        wON = true;
    }
}
