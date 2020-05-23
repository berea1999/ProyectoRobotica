using JetBrains.Annotations;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Cuerpo : MonoBehaviour
{
    public float rotacion = 80;
    public float movimiento = 50;

    public GameObject Brazo;
    public GameObject Objeto;

    float rotacionX=0;


    // Start is called before the first frame update
    void Start()
    {
        transform.position = new Vector3(0f, 7.95f, 0f);
    }

    // Update is called once per frame
    void Update()
    {
        Movimiento();
        Rotacion();
        rotacionX = Brazo.transform.eulerAngles.x;
        //print("X " + rotacionX);
    }

    void Movimiento()
    { 
        if (Input.GetKey(KeyCode.UpArrow) && rotacionX<=0.01f)
            transform.Translate(Vector3.forward * movimiento * Time.deltaTime); //mover adelante

        if (Input.GetKey(KeyCode.DownArrow) && rotacionX<=0.01f)
            transform.Translate(Vector3.back * movimiento * Time.deltaTime); //mover atras
    }

    void Rotacion()
    {
        if (Input.GetKey(KeyCode.RightArrow))
            transform.Rotate(new Vector3(0f, rotacion, 0f) * Time.deltaTime); //rotar derecha

        if (Input.GetKey(KeyCode.LeftArrow))
            transform.Rotate(new Vector3(0f, -rotacion, 0f) * Time.deltaTime); //rotar izquierda

        //Movimiento hacia atrás la rotación se invierte
        if (Input.GetKey(KeyCode.RightArrow) && Input.GetKey(KeyCode.DownArrow) && !Input.GetKey(KeyCode.UpArrow))
            transform.Rotate(new Vector3(0f, -rotacion * 2, 0f) * Time.deltaTime); //rotar derecha

        if (Input.GetKey(KeyCode.LeftArrow) && Input.GetKey(KeyCode.DownArrow) && !Input.GetKey(KeyCode.UpArrow))
            transform.Rotate(new Vector3(0f, rotacion * 2, 0f) * Time.deltaTime); //rotar izquierda


    }

    void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject)
        {
            Debug.Log("Collision Detected");
        }
    }


}
