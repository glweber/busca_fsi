<!-- Improved compatibility of back to top link: See: https://github.com/glweber/busca_fsi/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the busca_fsi. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">


<h3 align="center">Rally - Map Generator Coupled with Search Algorithms</h3>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

This project is a map (graph) generator that incorporates uninformed search algorithms to find the optimal path between
two nodes.

## Key Features

- **Map Generation (Graph):** The map is generated based on user-defined parameters.

- **Search Algorithms:** The program includes both uninformed and informed search algorithms.

- **Map Visualization:** Users can visualize the map with or without the route calculated by the algorithm, along with
  the cost and the path to be taken.

- **Random Values:** Each edge has predefined values randomly assigned to them.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

![Python][Python.lg]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

To execute the project, please follow the steps below:

### Prerequisites

It is necessary to have the libraries used in the project installed in your environment. You can install them using pip
and the dependency file provided within the project.

* Installing the libraries using pip:
  ```sh
  pip install -r requirements.txt
  ```
* Creating a virtual environment:
  ```sh
  python -m venv venv_name
  source venv_name/bin/activate
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

To start the application, run the main.py file:

```sh
  python main.py
```

After execution, a window will appear on your screen, containing several fields that need to be filled out:

* Número de PSDP: Defines the number of nodes the graph will have.
* Razão de desconto: A decimal value that controls the discount for PSDP.
* Número de caminhos para cada PSDP: The number of edges at each node.

<p align="center">
  <img src="/img/menu1.png"/>
</p>


After filling in the fields, when you click on the 'Gerar Mapa' button, another window will open, displaying the created
graph:

<p align="center">
  <img src="/img/mapa.png"/>
</p>

When you click the 'Abrir Menu do Road Book' button, a third menu will open, allowing you to choose the starting and
ending nodes (PSDP de largada e chegada, respectively), as well as the search algorithm that will be used to determine
the optimal path.

<p align="center">
  <img src="/img/roadbook.png"/>
</p>

After selecting the desired search algorithm, the map with the optimal path will be displayed.

<p align="center">
  <img src="/img/path.png" />
</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

Guilherme Weber - weba.guilherme@outlook.com

Project Link: [https://github.com/glweber/busca_fsi](https://github.com/glweber/busca_fsi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/glweber/busca_fsi.svg?style=for-the-badge

[contributors-url]: https://github.com/glweber/busca_fsi/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/glweber/busca_fsi.svg?style=for-the-badge

[forks-url]: https://github.com/glweber/busca_fsi/network/members

[stars-shield]: https://img.shields.io/github/stars/glweber/busca_fsi.svg?style=for-the-badge

[stars-url]: https://github.com/glweber/busca_fsi/stargazers

[issues-shield]: https://img.shields.io/github/issues/glweber/busca_fsi.svg?style=for-the-badge

[issues-url]: https://github.com/glweber/busca_fsi/issues

[license-shield]: https://img.shields.io/github/license/glweber/busca_fsi.svg?style=for-the-badge

[license-url]: https://github.com/glweber/busca_fsi/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/glweber

[product-screenshot]: src/img/screenshot.png

[Python.lg]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[Python_url]: www.python.org
