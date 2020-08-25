/**
 * @author zhixin wen <wenzhixin2010@gmail.com>
 * version: 1.16.0
 * https://github.com/wenzhixin/bootstrap-table/
 */
.bootstrap-table .fixed-table-toolbar::after {
  content: "";
  display: block;
  clear: both;
}

.bootstrap-table .fixed-table-toolbar .bs-bars,
.bootstrap-table .fixed-table-toolbar .search,
.bootstrap-table .fixed-table-toolbar .columns {
  position: relative;
  margin-top: 10px;
  margin-bottom: 10px;
}

.bootstrap-table .fixed-table-toolbar .columns .btn-group > .btn-group {
  display: inline-block;
  margin-left: -1px !important;
}

.bootstrap-table .fixed-table-toolbar .columns .btn-group > .btn-group > .btn {
  border-radius: 0;
}

.bootstrap-table .fixed-table-toolbar .columns .btn-group > .btn-group:first-child > .btn {
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}

.bootstrap-table .fixed-table-toolbar .columns .btn-group > .btn-group:last-child > .btn {
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}

.bootstrap-table .fixed-table-toolbar .columns .dropdown-menu {
  text-align: left;
  max-height: 300px;
  overflow: auto;
  -ms-overflow-style: scrollbar;
  z-index: 1001;
}

.bootstrap-table .fixed-table-toolbar .columns label {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.428571429;
}

.bootstrap-table .fixed-table-toolbar .columns-left {
  margin-right: 5px;
}

.bootstrap-table .fixed-table-toolbar .columns-right {
  margin-left: 5px;
}

.bootstrap-table .fixed-table-toolbar .pull-right .dropdown-menu {
  right: 0;
  left: auto;
}

.bootstrap-table .fixed-table-container {
  position: relative;
  clear: both;
}

.bootstrap-table .fixed-table-container .table {
  width: 100%;
  margin-bottom: 0 !important;
}

.bootstrap-table .fixed-table-container .table th,
.bootstrap-table .fixed-table-container .table td {
  vertical-align: middle;
  box-sizing: border-box;
}

.bootstrap-table .fixed-table-container .table thead th {
  vertical-align: bottom;
  padding: 0;
  margin: 0;
}

.bootstrap-table .fixed-table-container .table thead th:focus {
  outline: 0 solid transparent;
}

.bootstrap-table .fixed-table-container .table thead th.detail {
  width: 30px;
}

.bootstrap-table .fixed-table-container .table thead th .th-inner {
  padding: 0.75rem;
  vertical-align: bottom;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.bootstrap-table .fixed-table-container .table thead th .sortable {
  cursor: pointer;
  background-position: right;
  background-repeat: no-repeat;
  padding-right: 30px !important;
}

.bootstrap-table .fixed-table-container .table thead th .both {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAATCAQAAADYWf5HAAAAkElEQVQoz7X QMQ5AQBCF4dWQSJxC5wwax1Cq1e7BAdxD5SL+Tq/QCM1oNiJidwox0355mXnG/DrEtIQ6azioNZQxI0ykPhTQIwhCR+BmBYtlK7kLJYwWCcJA9M4qdrZrd8pPjZWPtOqdRQy320YSV17OatFC4euts6z39GYMKRPCTKY9UnPQ6P+GtMRfGtPnBCiqhAeJPmkqAAAAAElFTkSuQmCC");
}

.bootstrap-table .fixed-table-container .table thead th .asc {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAATCAYAAAByUDbMAAAAZ0lEQVQ4y2NgGLKgquEuFxBPAGI2ahhWCsS/gDibUoO0gPgxEP8H4ttArEyuQYxAPBdqEAxPBImTY5gjEL9DM+wTENuQahAvEO9DMwiGdwAxOymGJQLxTyD+jgWDxCMZRsEoGAVoAADeemwtPcZI2wAAAABJRU5ErkJggg==");
}

.bootstrap-table .fixed-table-container .table thead th .desc {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAATCAYAAAByUDbMAAAAZUlEQVQ4y2NgGAWjYBSggaqGu5FA/BOIv2PBIPFEUgxjB+IdQPwfC94HxLykus4GiD+hGfQOiB3J8SojEE9EM2wuSJzcsFMG4ttQgx4DsRalkZENxL+AuJQaMcsGxBOAmGvopk8AVz1sLZgg0bsAAAAASUVORK5CYII= ");
}

.bootstrap-table .fixed-table-container .table tbody tr.selected td {
  background-color: rgba(0, 0, 0, 0.075);
}

.bootstrap-table .fixed-table-container .table tbody tr.no-records-found td {
  text-align: center;
}

.bootstrap-table .fixed-table-container .table tbody tr .card-view {
  display: flex;
}

.bootstrap-table .fixed-table-container .table tbody tr .card-view .card-view-title {
  font-weight: bold;
  display: inline-block;
  min-width: 30%;
  text-align: left !important;
}

.bootstrap-table .fixed-table-container .table .bs-checkbox {
  text-align: center;
}

.bootstrap-table .fixed-table-container .table .bs-checkbox label {
  margin-bottom: 0;
}

.bootstrap-table .fixed-table-container .table .bs-checkbox label input[type="radio"],
.bootstrap-table .fixed-table-container .table .bs-checkbox label input[type="checkbox"] {
  margin: 0 auto !important;
}

.bootstrap-table .fixed-table-container .table.table-sm .th-inner {
  padding: 0.3rem;
}

.bootstrap-table .fixed-table-container.fixed-height:not(.has-footer) {
  border-bottom: 1px solid #dee2e6;
}

.bootstrap-table .fixed-table-container.fixed-height.has-card-view {
  border-top: 1px solid #dee2e6;
  border-bottom: 1px solid #dee2e6;
}

.bootstrap-table .fixed-table-container.fixed-height .fixed-table-border {
  border-left: 1px solid #dee2e6;
  border-right: 1px solid #dee2e6;
}

.bootstrap-table .fixed-table-container.fixed-height .table thead th {
  border-bottom: 1px solid #dee2e6;
}

.bootstrap-table .fixed-table-container.fixed-height .table-dark thead th {
  border-bottom: 1px solid #32383e;
}

.bootstrap-table .fixed-table-container .fixed-table-header {
  overflow: hidden;
}

.bootstrap-table .fixed-table-container .fixed-table-body {
  overflow-x: auto;
  overflow-y: auto;
  height: 100%;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading {
  align-items: center;
  background: #fff;
  display: none;
  justify-content: center;
  position: absolute;
  bottom: 0;
  width: 100%;
  z-index: 1000;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading .loading-wrap {
  align-items: baseline;
  display: flex;
  justify-content: center;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading .loading-wrap .loading-text {
  font-size: 2rem;
  margin-right: 6px;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading .loading-wrap .animation-wrap {
  align-items: center;
  display: flex;
  justify-content: center;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading .loading-wrap .animation-dot,
.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading .loading-wrap .animation-wrap::after,
.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading .loading-wrap .animation-wrap::before {
  content: "";
  animation-duration: 1.5s;
  animation-iteration-count: infinite;
  animation-name: LOADING;
  background: #212529;
  border-radius: 50%;
  display: block;
  height: 5px;
  margin: 0 4px;
  opacity: 0;
  width: 5px;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading .loading-wrap .animation-dot {
  animation-delay: 0.3s;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading .loading-wrap .animation-wrap::after {
  animation-delay: 0.6s;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading.table-dark {
  background: #212529;
}

.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading.table-dark .animation-dot,
.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading.table-dark .animation-wrap::after,
.bootstrap-table .fixed-table-container .fixed-table-body .fixed-table-loading.table-dark .animation-wrap::before {
  background: #fff;
}

.bootstrap-table .fixed-table-container .fixed-table-footer {
  overflow: hidden;
}

.bootstrap-table .fixed-table-pagination::after {
  content: "";
  display: block;
  clear: both;
}

.bootstrap-table .fixed-table-pagination > .pagination-detail,
.bootstrap-table .fixed-table-pagination > .pagination {
  margin-top: 10px;
  margin-bottom: 10px;
}

.bootstrap-table .fixed-table-pagination > .pagination-detail .pagination-info {
  line-height: 34px;
  margin-right: 5px;
}

.bootstrap-table .fixed-table-pagination > .pagination-detail .page-list {
  display: inline-block;
}

.bootstrap-table .fixed-table-pagination > .pagination-detail .page-list .btn-group {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}

.bootstrap-table .fixed-table-pagination > .pagination-detail .page-list .btn-group .dropdown-menu {
  margin-bottom: 0;
}

.bootstrap-table .fixed-table-pagination > .pagination ul.pagination {
  margin: 0;
}

.bootstrap-table .fixed-table-pagination > .pagination ul.pagination a {
  padding: 6px 12px;
  line-height: 1.428571429;
}

.bootstrap-table .fixed-table-pagination > .pagination ul.pagination li.page-intermediate a {
  color: #c8c8c8;
}

.bootstrap-table .fixed-table-pagination > .pagination ul.pagination li.page-intermediate a::before {
  content: '\2B05';
}

.bootstrap-table .fixed-table-pagination > .pagination ul.pagination li.page-intermediate a::after {
  content: '\27A1';
}

.bootstrap-table .fixed-table-pagination > .pagination ul.pagination li.disabled a {
  pointer-events: none;
  cursor: default;
}

.bootstrap-table.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1050;
  width: 100% !important;
  background: #fff;
  height: calc(100vh);
  overflow-y: scroll;
}

/* calculate scrollbar width */
div.fixed-table-scroll-inner {
  width: 100%;
  height: 200px;
}

div.fixed-table-scroll-outer {
  top: 0;
  left: 0;
  visibility: hidden;
  width: 200px;
  height: 150px;
  overflow: hidden;
}

@keyframes LOADING {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
