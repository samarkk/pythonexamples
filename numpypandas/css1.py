'''
<style>
*{
font-size: 16px;
}
#notebook-container {
  box-shadow: none !important;
}

.container {
  width: 90% !important;
}

.notebook_app {
  background: #fff !important;
}

body > #header {
  background: lightblue;
}

.navbar-default {
  background: none;
  border: none;
}

.navbar-default .navbar-nav > li > a, #kernel_indicator {
  /* color: rgba(255, 255, 255, 0.25);*/
  /* color: black;*/
  font-weight: bold;
  border-bottom: 2px solid #f57b00;
  transition: all 0.25s;
}

.navbar-default .navbar-nav > li > a:hover,
#kernel_indicator:hover {
  border-bottom: 2px solid #fff;
  color: rgba(255, 255, 255, 1);
}

div.input_area {
  border: none;
  border-radius: 0;
  background: #f7f7f7;
  line-height: 1.5em;
  margin: 0.5em 0;
  padding: 0;
  
}

div.cell {
  transition: all 0.25s;
  border: none;
  position: relative;
  top: 0;
}

div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border: none; 
  background: transparent;
  box-shadow: 0 6px 18px #aaa;
  z-index: 10;
  top: -10px;
}

div#pager {
  opacity: 0.85;
  z-index: 9999;
}

.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  color: #fff;
  background-color: transparent;
  border-bottom: 2px solid #fff;
}

.dropdown-menu {
  z-index: 999999 !important;
  background-color: #f57b00;
  opacity: 0.95;
}

.dropdown-menu > li > a {
  color: #fff;
}

.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: rgba(255, 255, 255, 0.25);
}

.navbar-nav > li > .dropdown-menu {
  border: none;
  box-shadow: none;
}

div.output_wrapper {
  background:  #eee;
  border: 1px solid green;
  border-radius: 2px;
}

div.cell.unselected div.output_area {
  box-shadow: inset 0 0 25px #aaa;
  padding: 1em 0;
  overflow-x: auto;
  transition: all 0.25s;
}

div.cell.selected .output_area {
  box-shadow: inset 0 0 5px #aaa;
  padding: 0.5em 0;
  overflow-x: auto;
}

div.cell.selected .div.output_scroll {
  box-shadow: none;
}

div.output_wrapper {
  margin: 0 0 1em;
  transition: all 0.25s;
}

div.cell.selected .output_wrapper {
  margin: 0;
}

.dataframe {
  background: #fff;
  box-shadow: 0px 1px 2px #bbb;
}

.dataframe thead th,
.dataframe tbody td {
  text-align: right;
  padding: 1em;
}

.output,
div.output_scroll {
  box-shadow: none;
}

.rendered_html pre code {
  background: #f4f4f4;
  border: 1px solid #ddd;
  border-left: 3px solid #2a7bbd;
  color: #444;
  page-break-inside: avoid;
  font-family: monospace;
  font-size: 15px;
  line-height: 1.6;
  margin-bottom: 1.6em;
  max-width: 100%;
  overflow: auto;
  padding: 1em 1.5em;
  display: block;
  word-wrap: break-word;
}

h1,
.h1 {
  font-size: 33px;
  font-family: "Trebuchet MS";
  font-size: 2.5em !important;
  color: #2a7bbd;
}
</style>
'''