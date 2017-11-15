
% include('head.tpl', title='Lime Registration')

% rebase('index.tpl')

% nick = 'Nick'
% password = 'Password'
% twopass = 'Password repeat'

<div id="coord_property">
    <form id="register_lime" action="/newaccount" enctype="multipart/form-data" method="post">
        <p>
            <input id="check1" type="text" autocomplete="off" name="sheet" placeholder="{{ nick }}" required />
        </p>
        <p>
            <input id="check2" type="text"  autocomplete="off" name="sheet" placeholder="{{ password }}" required />
        </p>
        <p>
            <input id="check3" type="text"  autocomplete="off" name="sheet" placeholder="{{ twopass }}" required />
        </p>
    </form>
</div>
