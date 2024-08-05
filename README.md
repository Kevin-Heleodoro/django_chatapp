# DJ Chat

Routes:

http://localhost:8000/admin/

http://localhost:8000/api/docs/schema/ui

http://localhost:8000/api/server/select/
http://localhost:8000/api/server/select/?qty=1
http://localhost:8000/api/server/select/?with_num_members=true
http://localhost:8000/api/server/select/?category=cat2
http://localhost:8000/api/server/select/?by_user=true
http://localhost:8000/api/server/select/?by_serverid=2

Need to look at the possible combinations in the ServerListViewSet.list method for which parameters should not work together

http://localhost:5173/

To run:

backend: `./manage.py runserver`

frontend: `npm run dev`
