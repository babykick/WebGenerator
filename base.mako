<%inherit file="base.html.mako" />

<%block name="title">
    ${page.title}
</%block>
 
 <%block name="css">
    % for css in page.cssFiles:
       <link rel="stylesheet" href="${css}" type="text/css" media="screen" />
    % endfor
 </%block>
 
 <%block name="script">
     % for js in page.jsFiles:
        <script type="text/javascript" src="${js}"></script>
     % endfor
 </%block>
 
<%block name="navlist">
   <ul>
      % for link in page.nav.links:
        <li class="page_item"><a href="${link[1]}">${link[0]}</a></li>
      % endfor
  </ul>

</%block> 
 
<%block name="content">
  % for post in page.posts:
  <div class="post">
      <h2><a href="#"> ${post.title}</a><br></h2>
      <p>
           % for image in post.images:
               <img src="${imgdir}/${image['name']}" id="${image['name']}" alt="${image['name']}" width="${image['width']}px" />
           % endfor
           ${post.content}
      </p>

  </div>
  % endfor
 

</%block>

<%block name="sidebarinfo">
   <ul>
     <li> Student Name: ${page.designer.name} </li>
     <li> Student ID: ${page.designer.id} </li>
     <li> Course: ${page.designer.course} </li>
   </ul>
 
</%block>

<%block name="footer">
   <p> Designed by ${page.designer.name} </p>
</%block>
