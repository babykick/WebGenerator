<%inherit file="base.html" />

<%block name="title">
    ${student.name}: ${student.course}
</%block>
 
<%block name="navlist">
   <ul>
      % for link in links:
        <li class="page_item"><a href="${link[1]}">${link[0]}</a></li>
      % endfor
  </ul>

</%block> 
 
<%block name="content">
  % for post in posts:
  <div class="post">
      <h2><a href="#"> ${post.title}</a><br></h2>
      <p>
           % for image in post.images:
               <img src="${imgdir}/${image}" />
           % endfor
           ${post.content}
      </p>
  % endfor
  </div>  
 

</%block>

<%block name="sidebarinfo">
   <ul>
     <li> Student Name: ${student.name} </li>
     <li> Course: ${student.course} </li>
   </ul>
 
</%block>


