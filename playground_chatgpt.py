# def reject_requests(requests, limit_per_sec):
#     # Create a dictionary to keep track of request counts for each user IP
#     user_ips = {}
#     # Create a list to keep track of rejected request IDs
#     rejected = []
#     for request in requests:
#         # Split the request string into its components
#         request_id, user_ip, unix_time_stamp = request.split()
#         # Convert user_ip and unix_time_stamp to integers
#         user_ip = int(user_ip)
#         unix_time_stamp = int(unix_time_stamp)
#         # Check if this user IP has exceeded the limit_per_sec
#         if user_ip in user_ips and unix_time_stamp - user_ips[user_ip] < 1000 / limit_per_sec:
#             # Add this request ID to the rejected list
#             rejected.append(request_id)
#         else:
#             # Update the user_ips dictionary with the current request's unix_time_stamp
#             user_ips[user_ip] = unix_time_stamp
#     return rejected

# def reject_requests(requests, limit_per_sec):
#     last_request_time = {}
#     rejected = []
#     for request in requests:
#         request_id, user_ip, unix_time_stamp = map(int, request.split())
#         if user_ip in last_request_time:
#             time_diff = unix_time_stamp - last_request_time[user_ip]
#             if time_diff < 1000 / limit_per_sec:
#                 rejected.append(str(request_id))
#         last_request_time[user_ip] = unix_time_stamp
#     return rejected

# def reject_requests(requests, limit_per_sec):
#     last_request_time = {}
#     request_count = {}
#     rejected = []
#     for request in requests:
#         request_id, user_ip, unix_time_stamp = map(int, request.split())
#         if user_ip in last_request_time:
#             time_diff = unix_time_stamp - last_request_time[user_ip]
#             if time_diff < 1000 / limit_per_sec:
#                 if user_ip in request_count and request_count[user_ip] >= limit_per_sec:
#                     rejected.append(str(request_id))
#                 else:
#                     request_count[user_ip] += 1
#             else:
#                 request_count[user_ip] = 1
#         else:
#             request_count[user_ip] = 1
#         last_request_time[user_ip] = unix_time_stamp
#     return rejected

from collections import deque

def reject_requests(requests, limit_per_sec):
    # Create a dictionary to keep track of requests for each user IP
    requests_by_ip = {}
    # Create a dictionary to keep track of the most recent request time for each user IP
    last_request_time_by_ip = {}
    # Create a deque to keep track of the request IDs to be rejected
    rejected_request_ids = deque()

    for request in requests:
        # Split the request into its components
        request_id, user_ip, request_time = request.split(' ')
        request_id = int(request_id)
        request_time = int(request_time)

        # Check if the user IP has any requests
        if user_ip in requests_by_ip:
            # Check if the user IP has made too many requests in the last second
            while len(requests_by_ip[user_ip]) > 0 and request_time - requests_by_ip[user_ip][0] >= 1000:
                requests_by_ip[user_ip].popleft()

            if len(requests_by_ip[user_ip]) >= limit_per_sec:
                rejected_request_ids.append(request_id)
            else:
                requests_by_ip[user_ip].append(request_time)
        else:
            requests_by_ip[user_ip] = deque([request_time])

    return list(rejected_request_ids)

requests = ["1 12345 5000", "2 12345 5500", "3 12345 6000", "4 12345 7000", "5 12345 7000", "6 123 7400", "7 12345 7500", "8 12345 8000"]
limit_per_sec = 1
rejected = reject_requests(requests, limit_per_sec)
print(rejected)  # Output: ['2', '5', '7']

limit_per_sec = 2
rejected = reject_requests(requests, limit_per_sec)
print(rejected)  # Output: ['7']