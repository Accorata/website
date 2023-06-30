var list = document.getElementById('list');

function add_to_list(name) {
  let new_elem = document.createElement('tr');
  let new_elem_descrip = document.createElement('th');
  new_elem_descrip.setAttribute("scope", "row");
  let new_elem_descrip_text = document.createTextNode("1");
  new_elem_descrip.appendChild(new_elem_descrip_text);
  new_elem.appendChild(new_elem_descrip);
  for (let i = 0; i < name.length; i++) {
    let new_elem_list_elem = document.createElement('td');
    let new_elem_list_elem_text = document.createTextNode(name[i]);
    new_elem_list_elem.appendChild(new_elem_list_elem_text);
    new_elem.appendChild(new_elem_list_elem);
  }

  list.appendChild(new_elem);
  return true;
}

add_to_list(["a"]);
